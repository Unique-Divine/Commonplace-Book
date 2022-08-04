# drift-protocol.md           <!-- omit in toc -->

Drift Protocol is an open-sourced decentralized exchange on Solana powering the novel Dynamic AMM (DAMM) in addition to a decentralized orderbook (DLOB). Drift's first product is perpetual swaps, similar to what you see on Binance, FTX, and Huobi. 

Table of Contents
- [Drift Qualitative Analysis](#drift-qualitative-analysis)
    - [Q: Why did Drift make a perpetual swap exchange?](#q-why-did-drift-make-a-perpetual-swap-exchange)
    - [Q: Why did Drift decide to build perps?](#q-why-did-drift-decide-to-build-perps)
    - [Q: Why build perps fully on-chain?](#q-why-build-perps-fully-on-chain)
- [Dynamic Automated Market Maker (DAMM)](#dynamic-automated-market-maker-damm)
  - [Slippage and Virtual AMM pools](#slippage-and-virtual-amm-pools)
  - [Effects of Altering the Swap Invariant](#effects-of-altering-the-swap-invariant)
    - [Dangers of Increasing or Decreasing `k`](#dangers-of-increasing-or-decreasing-k)
- [Dynamically adjusting the  swap invariant (`k`)](#dynamically-adjusting-the--swap-invariant-k)
  - [Code Implementation - Dynamic `k`](#code-implementation---dynamic-k)
- [Funding Payments on Drift](#funding-payments-on-drift)
- [Rebates](#rebates)
- [Repegging, a.k.a Drift Cover - Drift V1](#repegging-aka-drift-cover---drift-v1)
  - [Code Notes - Repegging](#code-notes---repegging)
    - [`#[derive(Default)]`](#derivedefault)
    - [Traits](#traits)
- [Technical Incident: Withdrawal Bug](#technical-incident-withdrawal-bug)
- [Resources](#resources)

--- 

# Drift Qualitative Analysis

#### Quick primer on perpetual swaps

Perps are a very crypto native invention. They came out around 2016/2017 and were invented by BitMex. No cash is exchanged with a perpetual swap. A perp is a futures contract that never expires. Counterparties are not needed as the swap can be done with the exchange. 

The bane of perpetual swaps existence is the mechanism for keeping the price of the derivative in line with oracle prices. This is called the funding rate. 

Funding rates are essentially charged to participants who are on the wrong side or the aggressive side of the contract. For example, if there's a $1000 difference between the mark and index prices, the goal is to make this difference amortized over a period of 24 hours. Some exchanges do continuous funding. Some do 8 hour chunks. If the mark price is above the oracle price, people who are long the contract pay the funding rate.

Think of funding rate like a penalty for being against the oracle.  This incentives arbitrageurs to come in and correct the trade because they know that they can collect the funding rate as a reward for making the markets more in line with each other.

#### Background on the Drift team

Drift has a team of four co-founders with a mixture of trading, traditional finance, crypto, and software engineering backgrounds. 

Cindy Leow is one of the cofounders of Drift Protocol. She began in the crypto space in 2016 and started out trading as an exchange student in Korea. She noticed huge spreads betweeen US and Korean markets for BTC, sometimes as much as a 30% gap between the two. Cindy would use a Korean and American bank account to buy a coin in the US and sell it in Korea. Over time, she delved into other trading opportunities and found other market inefficiencies in crypto.

Then, she started automating on-chain strategies. Cindy started running a small prop fund and then got into DeFi during 2021.

#### What is meant by "delta one product"?

A delta one product is a a product that gives the investor the same exposure as if she were to own the underlying asset. A non-delta one product could something liek an option with an asymmetric payoff, causing price changes in the derivative to be different from the underlying asset.

Examples: All of the below examples give the investor exposure on the index, while outsourcing the actual replication  to another party.
- Exactly replicating an index: An investor would like to “own” the S&P500. The first alternative for the investor would be to buy all the 500 different shares that make up the S&P500, in the same proportions as the S&P500. If done correctly, the returns to the investor will now be the same as the return of the index. 
- Buy shares in an exchange traded fund (ETF) that tracks the underlying
- Buy futures on the underlying
- Trade an Index Swap derivative: This index swap would be designed to give the same returns, as if the investor were to own the index 

Ref: [Delta One Trading](https://www.fe.training/free-resources/financial-markets/delta-one-trading/)

#### Convex Product

- TODO describe convexity

### Q: Why did Drift make a perpetual swap exchange?

They wanted to do options early on but decided that perpetual swaps were a lot more liquid and easier to implement than standard options. Given how much bigger the market for perps is, the team assumed it would be easier and more condusive to growth to start with a delta one product rather than a convex product. 

The Drift founders decided to focus on building out the margining engine of the perps because it can be used to expand to other types of derivatives in the future. E.g., things like power perps, perps that track the square root of the underlying, or NFT floor perps. Those are some innovations Drift wants to build in the future. They wanted to start out with a  simple delta-one product as a base.

- ref: Floor Perps. Dave White: https://www.paradigm.xyz/2021/08/floor-perps

### Q: Why did Drift decide to build perps?

- Perps are the killer product in crypto. They create the easiest way to get exposure on an asset. Speculatively, it's also the easiest way to hedge against other assets. The composability of perps makes them easy to integrate on-chain. 

- Perps enable traders to get leveraged exposure and provide incentives for arbitrage, bringing about additional captial efficiency.

- Perps have an elegance in that, if have an oracle and an underlying with a continuous numerical value, you can build a market on top of something. It doesn't have to be crypto. You could make perps for COVID 19 vaccination rates, for example. 


### Q: Why build perps fully on-chain?

Some of the biggest markets exist on Binance and FTX, for instance. In other words, major centralized exchanges. The reason to build perps on-chain goes back to why we care about decentralization in the first place: it's ironic that the most liquid contracts in crypto are hosted in a centralized context, where every single participant has to trust a centralized exchange to hold the funds, make sure that pricing is transparent, and they're not actually trading against client orders.

Q: client orders?

There've been a ton of cases where CEXs have been accused of front running their customer orders (customer order = client order), or running a B-book against customers to turn a profit.

Q: B-book?

This is a term from Forex trading. An "A-book" is a type of execution where orders are passed directly to a liquidity pool by the broker. With an A-book, the broker doesn't act as the trader's counterpary. This keeps the trader and broker form having a conflict of interest.   

A "B-book" is an order book where the traders are processed with a dealing desk (in-house) by the broker. Sometimes, B-book brokers are called market makers or fixed spread brokers.

An on-chain solution to this where everything from the matching engine all the way to price discovery and the way funds are held being truly decentralized ensures full participation in the crypto world and enables users to custody their own funds.

... TBC
<!-- TODO -->

---

# Dynamic Automated Market Maker (DAMM)

Trades on Drift are executed against a dynamic virtual AMM ("DAMM"). There are some assertions in the Drift docs I'd like to look more closely at. The following questions will motivate most of my research. 

Claims:
> - "The DAMM works to reduce slippage for traders over time".  
> - "The DAMM is adaptable to the demand for trading in the market".
> - "The DAMM reduces the oracle and terminal price divergence over time".

Questions:
- Q: <!-- TODO --> How does the DAMM reduce slippage?
- Q: <!-- TODO --> What is meant by "demand for trading" here? How is that measured?   
- Q: <!-- TODO --> What makes the DAMM "adaptable"? Does it adapt itself, or is it adapted (manually)?
- Q: <!-- TODO --> How exactly does the DAMM reduce the divergence between oracle and terminal price?

## Slippage and Virtual AMM pools

In the context of an AMM, slippage refers to the price delta that occurs when a submitted swap transaction is still pending. Every swap changes the ratio of a pool's reserves and, thus, its price. Because many swaps can be submitted in the same block, the mark price at which a swap executes may differ  from what it was when the transaction was submitted.  

Suppose we have a liquidity pool based on Uniswap's constant-product formula. 
$$ 
\begin{aligned}
&k :\text{swap invariant} \\ 
&x :\text{base asset reserves} \\ 
&y :\text{quote asset reserves} \\ 
\end{aligned} \\ 
\Delta x, \Delta y :\text{changes to the reserves when a user swaps} \\ 
k = xy = (x + \Delta x)(y + \Delta y).
$$ 
A **virtual pool** behaves just like a regular liquidity pool, except users can only deposit or withdraw the quote asset in exchange for exposure in the base asset.

#### Ex. `Slip` and `Front` both go long in the same block.

Here, a trader (named `Slip`) wants to purchase 10 $x$ tokens and the instantaneous price, `y / x`, is 1. Seeing this price and intending to buy 10 tokens, the trader puts 10 $y$ tokens into the trade ($\Delta y = 10$). 

$$
\begin{aligned}
& x = 200, \quad y = 200, \quad \Delta y = 10 \\
& \therefore \quad \Delta x = \left( \frac{ xy }{ y + \Delta y } \right) - x \approx -9.524 = -\text{submittedOut}
\end{aligned}
$$

Notice, however, that the amount of tokens received is not 10 but a number close to 10. This is because of how little liquidity there is in the pool. A higher value of $k$ would make the trade execute closer to the output amount expected from the instantaneous price. 

Now, another trader (named `Front`) may have submitted a transaction within the same block as `Slip`. Let's say that `Front`:

- has a transaction that executes first 
- takes 5x leverage of `Slip` when opening the position 
- uses the same margin amount as `Slip`

This implies that `Front` executes the following trade:
$$
\begin{aligned}
& x = 200, \quad y = 200, \quad \Delta y = 5 * (10) = 50 \\
& \therefore \quad \Delta x 
  = \left( \frac{ xy }{ y + \Delta y } \right) - x 
  = -40
\end{aligned}
$$
The trade that executes for `Slip` is then:
$$
\begin{aligned}
& x = 160, \quad y = 250, \quad \Delta y = 10 \\
& \therefore \quad \Delta x 
  = \left( \frac{ xy }{ y + \Delta y } \right) - x 
  \approx -6.154 = -\text{executedOut}
\end{aligned}
$$

`Slip` submitted the swap transaction expecting to get 9.524 tokens and ended up only receiving 6.154 tokens because of `Front`'s effect on the pool. This difference is referred to as slippage, which is usually expressed as a percentage. 

$$
\text{slippage}
= \frac{\text{submittedOut} - \text{executedOut}}{\text{submittedOut}} 
= \frac{9.524 - 6.154}{9.524} \approx 35.4\%
$$

In this case, we'd say that `Slip` incurred 35.4% slippage. 

---

## Effects of Altering the Swap Invariant

> "A high appetite for arbitraging volume per oracle price movement encourages us to support a higher `k`. In return, this provides lower slippage for traders." - Drift

First, let's prove this claim on reduced slippage. Take the example from the slippage section with the traders `Front` and `Slip`, except multiply `k` by 4 (multiply `x` and `y` by 2). 

Expected trade for `Slip`:

$$
\begin{aligned}
& x = 400, \quad y = 400, \quad \Delta y = 10 \\
& \implies \quad \Delta x 
  = \left( \frac{ xy }{ y + \Delta y } \right) - x 
  \approx -9.756 = -\text{submittedOut}
\end{aligned}
$$

`Front` ends up executing the transaction earlier in the block:
$$
\begin{aligned}
& x = 400, \quad y = 400, \quad \Delta y = 5 * (10) = 50 \\
& \implies \quad \Delta x 
  = \left( \frac{ xy }{ y + \Delta y } \right) - x 
  = -44.\bar{4} 
\end{aligned}
$$

Thus, `Slip`'s transaction executes with the effects from `Front`:
$$
\begin{aligned}
& x = 355.\bar{5}, \quad y = 450, \quad \Delta y = 10 \\
& \implies \quad \Delta x 
  = \left( \frac{ xy }{ y + \Delta y } \right) - x 
  \approx -7.729 = -\text{executedOut}
\end{aligned}
$$

$$
\text{slippage} 
= \frac{\text{submittedOut} - \text{executedOut}}{\text{submittedOut}} 
= \frac{9.524 - 6.154}{9.524} \approx 20.77\%
$$

By increasing `k` to `4k`, slippage decreased from 35.4\% to 20.77\%. In general, **slippage for the same submitted transaction decreases as we increase `k`**, holding all else constant.

Opening a position is synonymous with inputting a positive $\Delta y$ for a perpetual swap because it increases the reserves, while closing a position is synonymous with inputting a negative $\Delta y$ because it decreases the reserves. This means that **slippage can also occur when closing a position**. Increasing `k` lowers slippage risks while both closing and opening positions.

### Dangers of Increasing or Decreasing `k`

Q: What is the danger in increasing the swap invariant?

Altough increasing `k` lowers slippage, it makes the underlying virtual pool  operate like a real AMM pool with hhigher liquidity, meaning that it becomes harder to change the price. The main danger with inappropriately increasing `k` is that arbitrageurs may not have enough funds to align the mark price with the underlying index price.

#### Decreasing `k`

Drift "does not intend to decrease `k`", however it will in in the case of specific market conditions.

> "Our goal is to monotonically increase `k` (swap invariant) over time as the platform and open interest grows. `k` is bound by fees collected." - Drift

In the event of a "market failure", when arbitrage trading demand is not enough to converge the mark price to the oracle price, `k` may be lowered. This causes trades to have a larger effect on the mark price, making it easier for arbitragers to converge mark and index. 

# Dynamically adjusting the  swap invariant (`k`) 

At all times, the base reserve amount `x` and quote reserve amount  `y` obey the equation `xy = k`. This gives rise to an instantaneous price for the virtual pool, `y / x`. Altering `k` means changing `k` while holding the instantanous price constant. This is achieved by scaling both `x` and `y` by the same factor. 
$$
\begin{aligned}
&c :\text{scaling factor} \\ 
& \text{price} = \frac{y}{x} = \frac{cy}{cx} \\ 
& k = x y. \quad k' = (cx)(cy) = c^2k \\
\end{aligned}
$$

## Code Implementation - Dynamic `k`

Ref: `programs/clearing_house/src/lib.rs`
```rust
pub fn update_k(ctx: Context<AdminUpdateK>, sqrt_k: u128, market_index: u64) -> Result<()> { 
  //...
}
```

---

# Funding Payments on Drift

With a virtual AMM, there can be an imbalance between longs and shorts and funding can be asymmetric.
To account for this, `amm` keeps track of the cumulative funding rate for both longs and shorts.
When there is a period with asymmetric funding, the clearing house will either pay funding from its collected fee account or receive funding to the account.

Q: When do periods of asymmetric funding occur?       <!-- TODO -->

```ts
// Calculate the funding payment owed by the net_market_position if funding is not capped
// If the net market position owes funding payment, the clearing house receives payment
netMarketSize = market.baseAssetAmount // sum of all positions sizes
netMarketFundingPayment = fundingRateDelta * netMarketSize
```

Q: Why would the funding be capped? Where does the cap come from?      <!-- TODO -->

See 
```rust 
fn caclulate_capped_funding_rate(
  market: &Market,
  uncapped_funding_pnl: i128, // if negative, users would net recieve from clearinghouse
  funding_rate: i128,
) -> ClearingHouseResult<(i128, i128)> {
  //...
  Ok((capped_funding_rate, capped_funding_pnl))
}
```

The funding_rate_pnl_limit is the amount of fees the clearing house can use before it hits it's lower bound. The limit is capped at 2/3 of the current fee pool per funding period.



Q: When does the net user position owe funding versus receiving it?      <!-- TODO -->


---

# Rebates

> "Drift protocol mandates this temporary liquidity withholding to be used as a rebate at a later time for market's position holders, ensuring the eventual rebating of position holders." - Drift


On Drift, funding payments, repegs, and



---

# Repegging, a.k.a Drift Cover - Drift V1


Peg multiplier:

Suppose there is a two-dimensional constant product curve defined by the `x * y = k` swap invariant.
The market price for `x` in terms of `y` is the slope of the curve given the relative scarcity. 

```ts
price = (y / x) * C
// With verbose names, this is equivalent to
markPrice = (quoteReserves / baseReserves) * pegMultiplier 
```

The price can be multiplied by an arbitrary constant `C` (essentially a scaling factor for `y`).

TODO Q: "relative scarcity"?


## Code Notes - Repegging

Repo: [drift-labs/protocol-v1](https://github.com/drift-labs/protocol-v1)

- `docs/sdk`: HTML files for the Drift SDK documentation website.
- `cargo.toml`: The `Cargo.toml` file for a Rust package is called its manifest. The manifest is written in Tom's Obvious Minimal Language (TOML) format. It contains [these sections](https://doc.rust-lang.org/cargo/reference/manifest.html).
- `programs/clearing_house`: In Drift V1, the Rust code that defines the protocol lives in the `programs` directory. 
  

`clearing_house/src/math/repeg.rs`

```rust 
#[zero_copy]
#[derive(Default)]
#[repr(packed)]
pub struct Market {
  pub initialized: bool,
  pub base_asset_amount_long: i128,
  pub base_asset_amount_short: i128,
  pub base_asset_amount: i128, // net market bias
  pub open_interest: u128,     // number of users in a position
  pub amm: AMM,
  pub margin_ratio_initial: u32,
  pub margin_ratio_partial: u32,
  pub margin_ratio_maintenance: u32,

  // ...
}
```

Q: What does the `#[textHere]` syntax mean?

This is called an outer attribute for the structure definition.

### `#[derive(Default)]` 

> [`Default` is a trait](https://doc.rust-lang.org/std/default/trait.Default.html) for giving a type a useful default value. 
This section will give enough detail to understand `Default`. If you need more information on Rust traits in general, see [Traits](#traits).

```rust 
pub trait Default {
  fn default() -> Self;
}
```

Sometimes, you want to fall back to some kind of default value and don't particularly care what it is. This comes up often with structures:
```rust
struct SomeOptions {
  foo: i32,
  bar: f32,
}
```
You can use the `Default` trait to define default values for the `SomeOptions` structure. 
```rust
#[derive(Default)]
struct SomeOptions {
  foo: i32, 
  bar: f32,
}
```

Rust implements the `Default` trait for primitive types. To create an instance with all of the default values, use 
```rust
let options: SomeOptions = Default::default();
```

If, instead, you wanted to override the `foo` field while retaining the default values for all other fields:
```rust
let options: SomeOptions { foo: 42, ..Default::default() }
```

TODO Q: Why does this trait use the `derive` fn? Is that even a fn?

### Traits

Traits in Rust are similar to a feature called "interfaces" in other languages. A **trait** defines functionality a particular type has and can share with other types. We use traits to define shared behavior in an abstract way.




Using **trait bounds** allows us to specify that a generic type can be any type that has a certain behavior. For example, if we define a structure that has six legs  that has 


#### `#[zero_copy]`


```rust
pub adjust_peg_cost(market: &must Market, new_peg: u128) -> ClearingHouseResult<i28> {
  // ...
}
```

---
# Technical Incident: Withdrawal Bug

- See [`protocol-v1/tests/driftDrain.ts`](https://github.com/drift-labs/protocol-v1/blob/crispheaney/drift-drain/tests/driftDrain.ts)

- See [`protocol-v1/tests/driftDrain10M.ts`](https://github.com/drift-labs/protocol-v1/blob/crispheaney/drift-drain/tests/driftDrain10M.ts)

- See [Drift Protocol Technical Incident Report - 2022/05/11](https://driftprotocol.medium.com/drift-protocol-technical-incident-report-2022-05-11-eedea078b6d4) 

TODO notes


# Resources

- Drift's Dynamic AMM. https://docs.drift.trade/drifts-dynamic-amm
- [drift-labs/protocol-v1](https://github.com/drift-labs/protocol-v1): Rust code for the contracts
- [Drift Protocol Technical Incident Report - 2022/05/11](https://driftprotocol.medium.com/drift-protocol-technical-incident-report-2022-05-11-eedea078b6d4)
- Drift TypeScript SDK. [@drift-labs/sdk](https://www.npmjs.com/package/@drift-labs/sdk). 
- Examples for Drift TS SDK: [drift-labs/example-bots](https://github.com/drift-labs/example-bots)
- [drift-labs/driftpy](https://github.com/drift-labs/driftpy): Drift Python SDK


Date: 22年8月2日
Tags: ["drift", "DAMM", "perpetual swaps", "perps", "repeg", "drift cover", "withdrawal bug"]

---

