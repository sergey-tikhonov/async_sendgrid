import logging
from typing import Optional

import requests_async as requests


class SendgridAPI:
    def __init__(self, api_key):
        self._api_key = api_key
        self._url = f'https://api.sendgrid.com/v3/mail/send'
        self._useragent = 'async_sendgrid/0.0.1;python'

    @property
    def _default_headers(self):
        headers = {
            'Authorization': f'Bearer {self._api_key}',
            'User-agent': self._useragent,
            'Accept': 'application/json'
        }
        return headers

    async def send(
        self,
        *,
        from_email: str,
        to_email: str,
        subject: str,
        content: str,
        template_id: str,
        from_name: Optional[str] = None,
        to_name: Optional[str] = None,
        template_data=None,
    ):
        logging.info(f'Sending email to {to_email}')

        from_ = {'email': from_email}
        if from_name:
            from_['name'] = from_name

        to = {'email': to_email}
        if to_name:
            to['name'] = to_name

        template_data = template_data or {}

        message = {
            'personalizations': [
                {
                    'to': [to],
                    'dynamic_template_data': template_data,
                }
            ],
            'from': from_,
            'subject': subject,
            'template_id': template_id,
            'content': [{
                'type': 'text/html',
                'value': content
            }]
        }

        response = await requests.post(
            self._url,
            json=message,
            headers=self._default_headers
        )

        return response
