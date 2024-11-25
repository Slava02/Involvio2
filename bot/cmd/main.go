package main

import (
	"fmt"
	client "github.com/Slava02/Involvio/bot/clients"
	"github.com/Slava02/Involvio/bot/config"
	"github.com/Slava02/Involvio/bot/internal/app"
	"github.com/Slava02/Involvio/bot/internal/usecase"
	"github.com/Slava02/Involvio/bot/pkg/logger"
	"log"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	// Load environment variables
	cfg, err := config.LoadConfig()
	if err != nil {
		panic(fmt.Sprintf("failed to load config: %v", err))
	}

	err = Run(cfg)
	if err != nil {
		log.Fatal(err)
		return
	}

}

func Run(cfg *config.Config) error {
	// Initialize logger
	logger.SetupLogger(cfg)

	// Initialize the client
	cli, err := client.NewClientWithResponses("http://127.0.0.1:8000")
	if err != nil {
		panic(err)
	}

	// Initialize usercase
	uc := usecase.New(cli)

	// Run the application
	bot := app.New(cfg, uc)

	go func() {
		if err := bot.Start(); err != nil {
			log.Fatal(err)
		}
	}()

	quit := make(chan os.Signal, 1)
	signal.Notify(quit, os.Interrupt, syscall.SIGTERM)
	<-quit

	return nil
}
