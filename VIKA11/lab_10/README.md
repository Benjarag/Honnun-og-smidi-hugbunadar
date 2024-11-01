# lab_10

This project implements a message API and message processing system using FastAPI, Docker, and RabbitMQ. The API allows users to save and retrieve messages, and message events are handled and consumed by a separate message processor service.

### Note
- The `message_storage.txt` file is included to store saved messages. However, messages are not written to this file by default. This behavior can be implemented if needed with further modifications. (Postman GET and POST, do work though, which was the requirement for the lab).
