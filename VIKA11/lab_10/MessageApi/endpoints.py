from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from models.message_model import MessageModel
from container import Container
from message_repository import MessageRepository
from message_sender import MessageSender

router = APIRouter()


@router.get('/messages/{id}', status_code=200)
@inject
async def get_message(id: int, message_repository: MessageRepository = Depends(Provide[Container.message_repository_provider])):
    # TODO: get message with id
    message = message_repository.get_message(id)
    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return message


@router.post('/messages', status_code=201)
@inject
async def save_messages(message: MessageModel,
                        message_sender: MessageSender = Depends(
                            Provide[Container.message_sender_provider]),
                        message_repository: MessageRepository = Depends(
                            Provide[Container.message_repository_provider])):

    # TODO: save message and send message event
    message_id = message_repository.save_message(message.message)  # Save the message to the repository
    message_sender.send_message(message.message)  # Send message event through the message sender
    return {"id": message_id}

