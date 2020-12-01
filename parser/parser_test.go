package parser

import (
	"testing"

	postal "github.com/openvenues/gopostal/parser"
)

func TestConvertAddressHouse(t *testing.T) {
	pc := postal.ParsedComponent{Label: "house", Value: "test house"}
	spc := []postal.ParsedComponent{pc}
	c := make(chan Address)

	go convertAddress(spc, c)

	res := Address{}
	res = <-c

	if res.house != "test house" {
		t.Errorf("Expected 'test house' value for 'house' but got %+v", res.house)
	}
}

func TestConvertAddressCategory(t *testing.T) {
	pc := postal.ParsedComponent{Label: "category", Value: "test cat"}
	spc := []postal.ParsedComponent{pc}
	c := make(chan Address)

	go convertAddress(spc, c)

	res := Address{}
	res = <-c

	if res.category != "test cat" {
		t.Errorf("Expected 'test cat' value for 'category' but got %+v", res.category)
	}
}
