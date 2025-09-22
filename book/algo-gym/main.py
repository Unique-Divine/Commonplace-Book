from typing import Dict


def main():
    print("Hello from dsalgo!")

    d: Dict[str, int] = dict(a=0, b=1)

    print(f'a: {d.get("a")}')
    print(f'b: {d.get("b")}')
    print(f'c: {d.get("c")}')
    print(f'c (optional default 2nd arg := 42): {d.get("c", 42)}')


if __name__ == "__main__":
    main()
