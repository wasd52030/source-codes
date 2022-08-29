package main

type Number interface {
	int | int16 | int32 | int64 | float32 | float64
}
