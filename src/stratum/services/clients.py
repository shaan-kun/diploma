from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

import stratum.models.clients as models
import stratum.tables as tables
from ..database import get_session


class ClientService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, client_id: int) -> tables.Client:
        """Возвращает клиента по его id."""
        client = (
            self.session
            .query(tables.Client)
            .filter(tables.Client.client_id == client_id)
            .first()
        )

        if not client:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return client

    def get(self, client_id: int) -> tables.Client:
        """Возвращает клиента по его id."""
        return self._get(client_id)

    def get_list(self) -> list[tables.Client]:
        """Возвращает список клиентов."""
        clients = (
            self.session
            .query(tables.Client)
            .all()
        )

        if not clients:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return clients

    def get_by_company(self, company_id: int) -> list[tables.Client]:
        """Возвращает список клиентов компании по её id."""
        clients = (
            self.session
            .query(tables.Client)
            .filter(tables.Client.company_id == company_id)
            .all()
        )

        if not clients:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return clients
