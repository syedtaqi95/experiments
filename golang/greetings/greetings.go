package greetings

import (
	"errors"
	"fmt"
)

func Hello(name string) (string, error) {
	if name == "" {
		return "", errors.New("empty name")
	}

	// Return a greeting that embeds the name in the message.
	message := fmt.Sprintf("Hi, %v. Welcome!", name)
	return message, nil
}
