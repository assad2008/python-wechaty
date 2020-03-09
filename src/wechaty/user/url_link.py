"""
UrlLink for Contact Message
"""
from typing import Type, TypeVar
import requests
from ..config import log
from wechaty_puppet.url_link_payload import UrlLinkPayload

T = TypeVar("T", bound="UrlLink")


class UrlLink:
    """
    url_link object which handle the url_link content
    """
    def __init__(self, payload: UrlLinkPayload):
        """
        initialization
        :param payload:
        """
        self.payload: UrlLinkPayload = payload

    @classmethod
    def create(cls: Type[T], url: str):
        log.info("create url_link for %s",
                 url)
        res = requests.get(url)
        return res

    def __str__(self):
        """
        UrlLink string format output
        :return:
        """
        return "UrlLink<%s>" % self.payload.url

    def title(self) -> str:
        """
        get UrlLink title
        :return:
        """
        return self.payload.title

    def thumbnail_url(self):
        """
        get thumbnail url
        :return:
        """
        return self.payload.thumbnail_url

    def description(self):
        """
        get description
        :return:
        """
        self.payload.description