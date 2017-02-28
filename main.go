package main

import (
	"encoding/json"
	"fmt"
	//<<<<<<< HEAD
	"io/ioutil"
	"net/http"
	"os"
	"time"
	//	"reflect"
)

type Leg struct {
	Mode              string    `json:"mode"`
	ArrivalTime       time.Time `json:"arrival_time"`
	DepartureTime     time.Time `json:"departure_time"`
	DistanceMeters    int       `json:"distance_meters"`
	Duration          int       `json:"duration_seconds"`
	InStation         int       `json:"in_station_seconds"`
	InStationWalkKind int       `json:"in_station_walk_kind"`
}

type Legs struct {
	Legs []Leg
}

type Journey struct {
	ListLegs []Legs
}

func main() {
	var req string

	req = "https://citymapper.com/api/7/journeys?start=48.813896%2C2.392448&end=48.928378%2C2.1622&sname=7%20Rue%20Maurice%20Grandcoing%2C%20Ivry-sur-Seine&ename=81%20Avenue%20de%20Tobrouk%2C%20Sartrouville&region_id=fr-paris"
	//	fmt.Println(req)
	resp, err := http.Get(req)
	defer resp.Body.Close()
	if err != nil {
		os.Exit(1)
	}
	fmt.Println(resp.Body)
	var dat map[string]interface{}
	content, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		os.Exit(2)
	}
	if err := json.Unmarshal(content, &dat); err != nil {
		panic(err)
	}

	//sample := dat["journeys"][0]["legs"]
	//fmt.Println("%v")
	//	resp, err := soup.Get("https://xkcd.com")
	//	if err != nil {
	//		os.Exit(1)
	//	}
	//)

	//func makeUrl() string {
	//	coords := checkParams()
	//	if coords[0] != "-1" && coords[1] != "-1" {
	//		return "https://citymapper.com/directions?endcoord=" + coords[0] + "%2C" + coords[1]
	//	}
	//	return "-1"
	//}
	//
	//func checkParams() []string {
	//	if len(os.Args) > 1 {
	//		if len(os.Getenv(os.Args[1])) > 0 {
	//			coords := strings.Split(os.Getenv(os.Args[1]), ",")
	//			if len(coords) == 2 {
	//				return coords
	//			} else {
	//				fmt.Println("Invalid format for environment variable", os.Args[1])
	//			}
	//		} else {
	//			fmt.Println("No value found for environment variable", os.Args[1])
	//		}
	//	} else {
	//		fmt.Println("Invalid usage")
	//	}
	//	return []string{"-1", "-1"}
	//}
	//
	//
	//func main() {
	//	fmt.Println(makeUrl())
	//>>>>>>> 65a1a61c5c340d929a9d290c4c671b394abea9cb
}
