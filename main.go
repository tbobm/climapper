package main

import (
	"fmt"
	"os"
	"strings"
)

func makeUrl() string {
	coords := checkParams()
	if coords[0] != "-1" && coords[1] != "-1" {
		return "https://citymapper.com/directions?endcoord=" + coords[0] + "%2C" + coords[1]
	}
	return "-1"
}

func checkParams() []string {
	if len(os.Args) > 1 {
		if len(os.Getenv(os.Args[1])) > 0 {
			coords := strings.Split(os.Getenv(os.Args[1]), ",")
			if len(coords) == 2 {
				return coords
			} else {
				fmt.Println("Invalid format for environment variable", os.Args[1])
			}
		} else {
			fmt.Println("No value found for environment variable", os.Args[1])
		}
	} else {
		fmt.Println("Invalid usage")
	}
	return []string{"-1", "-1"}
}


func main() {
	fmt.Println(makeUrl())
}
