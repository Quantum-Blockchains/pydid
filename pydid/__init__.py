"""PyDID."""

import logging
from typing import Callable, List, Optional, Type

from .common import DIDError
from .did import DID, InvalidDIDError
from .did_url import DIDUrl, InvalidDIDUrlError
from .doc import corrections, generic
from .doc.builder import DIDDocumentBuilder
from .doc.doc import (
    BaseDIDDocument,
    BasicDIDDocument,
    DIDDocument,
    DIDDocumentError,
    NonconformantDocument,
)
from .resource import Resource
from .service import DIDCommService, Service
from .verification_method import (
    VerificationMaterial,
    VerificationMaterialUnknown,
    VerificationMethod,
)

__all__ = [
    "BasicDIDDocument",
    "DID",
    "DIDCommService",
    "DIDDocument",
    "DIDDocumentBuilder",
    "DIDDocumentError",
    "DIDError",
    "DIDUrl",
    "InvalidDIDError",
    "InvalidDIDUrlError",
    "Service",
    "VerificationMethod",
    "VerificationMaterial",
    "VerificationMaterialUnknown",
    "Resource",
    "generic",
    "corrections",
]


LOGGER = logging.getLogger(__name__)


def deserialize_document(
    value: dict,
    corrections: Optional[List[Callable]] = None,
    *,
    strict: bool = False,
    cls: Optional[Type[BaseDIDDocument]] = None,
) -> BaseDIDDocument:
    """Deserialize a document from a dictionary."""
    print("\033[31mdef deserialize_document()\033[0m")
    if corrections:
        print("\033[31mif correction\033[0m")
        for correction in corrections:
            value = correction(value)

    cls = cls or DIDDocument
    if strict:
        print("\033[31mif strict\033[0m")
        print("\033[31mcls: \033[0m", cls)
        tmp = cls.deserialize(value)
        # return cls.deserialize(value)
        print("\033[31mtmp: \033[0m", tmp)
        return tmp
    try:
        print("\033[31mtry\033[0m")
        return cls.deserialize(value)
    except ValueError as error:
        LOGGER.warning("Failed to deserialize document: %s", error)
        LOGGER.info("Parsing document as non-conformant doc")

    return NonconformantDocument.deserialize(value)
