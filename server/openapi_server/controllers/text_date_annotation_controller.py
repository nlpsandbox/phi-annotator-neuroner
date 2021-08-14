import connexion
import re

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.text_date_annotation_request import \
    TextDateAnnotationRequest  # noqa: E501
from openapi_server.models.text_date_annotation import TextDateAnnotation
from openapi_server.models.text_date_annotation_response import \
    TextDateAnnotationResponse  # noqa: E501
from openapi_server.neuroner import neuroner

def create_text_date_annotations():  # noqa: E501
    """Annotate dates in a clinical note

    Return the date annotations found in a clinical note # noqa: E501

    :rtype: TextDateAnnotations
    """
    if connexion.request.is_json:
        try:
            annotation_request = TextDateAnnotationRequest.from_dict(
                connexion.request.get_json())
            note = annotation_request._note
            matches = neuroner.annotate(note._text)

            annotations = []
            add_date_annotations(annotations, matches)
            res = TextDateAnnotationResponse(annotations)
            status = 200
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    else:
        status = 400
        res = Error("Bad request", status, "Missing body")
    return res, status


def add_date_annotations(annotations, matches):
    """
    Converts matches to TextDateAnnotation objects and adds them to the
    annotations array specified.
    """
    for match in matches:
        if match['type'] in ["DATE"]:
            annotations.append(TextDateAnnotation(
                start=match['start'],
                length=len(match['text']),
                text=match['text'],
                confidence=95.5
            ))
