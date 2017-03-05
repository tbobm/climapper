package main

import (
	"encoding/json"
	"fmt"
	//"github.com/tidwall/gjson"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
	"time"
)

type Leg struct {
	Mode              string
	ArrivalTime       time.Time
	DepartureTime     time.Time
	DistanceMeters    int
	Duration          int
	InStation         int
	InStationWalkKind int
}

type Legs struct {
	Legs []Leg
}

type Journey struct {
	ListLegs []Legs
}

func checkParams() []string {
	if len(os.Args) > 1 {
		if len(os.Getenv(os.Args[1])) > 0 {
			coords := strings.Split(os.Getenv(os.Args[1]), ",")
			if len(coords) == 2 {
				return coords
			} else {
				fmt.Println("Invalid format for environment variable", os.Args[1])
				os.Exit(10)
			}
		} else {
			fmt.Println("No value found for environment variable", os.Args[1])
			os.Exit(10)
		}
	} else {
		fmt.Println("Invalid usage")
		os.Exit(3)
	}
	return []string{"-1", "-1"}
}

func makeUrl() string {
	coords := checkParams()
	return "https://citymapper.com/directions?endcoord=" + coords[0] + "%2C" + coords[1]
}

func main() {
	var req string
	journeys := []Leg{}
	//	var dat map[string]interface{}

	req = "https://citymapper.com/api/7/journeys?start=48.813896%2C2.392448&end=48.928378%2C2.1622&sname=7%20Rue%20Maurice%20Grandcoing%2C%20Ivry-sur-Seine&ename=81%20Avenue%20de%20Tobrouk%2C%20Sartrouville&region_id=fr-paris"
	resp, err := http.Get(req)

	defer resp.Body.Close()
	if err != nil {
		os.Exit(1)
	}

	fmt.Println(resp.Body)

	content, err := ioutil.ReadAll(resp.Body) // Content to bytes

	if err != nil {
		os.Exit(2)
	}
	var data map[string][]map[string][]interface{}
	err = json.Unmarshal(content, &data)
	for i := range data["journeys"] {
		item := data["journeys"][i]["legs"]
		if item != nil {
			for j := range item {
				step := item[j]
				fmt.Println("%v", step)
			}
			os.Exit(0)
			//journeys = append(journeys, item)
		}
	}
	//if !ok {
	//fmt.Println("not a map")
	//fmt.Println(ok)
	//}
	fmt.Println(journeys[0])
}
