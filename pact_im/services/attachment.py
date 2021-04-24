from pact_im.services.base import Service


class AttachmentService(Service):
    ENDPOINT = 'companies/%s/conversations/%s/messages/attachments'
