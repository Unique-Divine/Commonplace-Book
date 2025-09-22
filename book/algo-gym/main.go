package main

import (
	"bytes"
	"fmt"
	"net/http"
)

func main() {
	// io.Reader
	// io.Writer
	bzReader := bytes.NewReader([]byte("payload"))
	bzReader.Read()

	fmt.Println("hello, world")

	httpRes, err := http.Get("foo.com")
	httpRes.Body.
}
