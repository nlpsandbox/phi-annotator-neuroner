import connexion
import re
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.text_contact_annotation_request import TextContactAnnotationRequest  # noqa: E501
from openapi_server.models.text_contact_annotation import TextContactAnnotation
from openapi_server.models.text_contact_annotation_response import TextContactAnnotationResponse  # noqa: E501
from openapi_server.neuroner import neuroner

def create_text_contact_annotations(text_contact_annotation_request=None):  # noqa: E501
    """Annotate contacts in a clinical note
    Return the Contact annotations found in a clinical note # noqa: E501
    :param text_contact_annotation_request:
    :type text_contact_annotation_request: dict | bytes
    :rtype: TextContactAnnotationResponse
    """
    if connexion.request.is_json:
        try:
            annotation_request = TextContactAnnotationRequest.from_dict(
                connexion.request.get_json())
            note = annotation_request._note
            matches = neuroner.annotate(note._text)

            annotations = []
            add_contact_annotations(annotations, matches)
            res = TextContactAnnotationResponse(annotations)
            status = 200
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    else:
        status = 400
        res = Error("Bad request", status, "Missing body")
    return res, status


def add_contact_annotations(annotations, matches):
    """
    Converts matches to TextContactAnnotation objects and adds them to the
    annotations array specified.
    """
    for match in matches:
        # TODO: Are there non-straightforward types that we can support?
        # TODO: Use "other" when applicable
        if match['type'] in ["PHONE","URL","EMAIL","FAX"]:
            annotations.append(TextContactAnnotation(
                start=match['start'],
                length=len(match['text']),
                text=match['text'],
                contact_type=match['type'].lower(),
                confidence=95.5
            ))
