import connexion
import pandas as pd
import re

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.text_location_annotation import TextLocationAnnotation  # noqa: E501
from openapi_server.models.text_location_annotation_request import TextLocationAnnotationRequest  # noqa: E501
from openapi_server.models.text_location_annotation_response import TextLocationAnnotationResponse  # noqa: E501
from openapi_server.neuroner import neuroner

def create_text_location_annotations():  # noqa: E501
    """Annotate locations in a clinical note

    Return the location annotations found in a clinical note # noqa: E501

    :param text_location_annotation_request:
    :type text_location_annotation_request: dict | bytes

    :rtype: TextLocationAnnotationResponse
    """
    res = None
    status = None
    if connexion.request.is_json:
        try:
            annotation_request = TextLocationAnnotationRequest.from_dict(
                connexion.request.get_json())
            note = annotation_request._note
            matches = neuroner.annotate(note._text)

            annotations = []
            add_location_annotations(annotations, matches)
            res = TextLocationAnnotationResponse(annotations)
            status = 200
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    else:
        status = 400
        res = Error("Bad request", status, "Missing body")
    return res, status


def add_location_annotations(annotations, matches):
    """
    Converts matches to TextLocationAnnotation objects and adds them
    to the annotations array specified.
    """
    for match in matches:
        # TODO Clarify types
        # TODO Does not annotate Seattle?
        if match['type'] in ["CITY","COUNTRY","STATE","STREET"]:
            annotations.append(
                TextLocationAnnotation(
                    start=match['start'],
                    length=len(match['text']),
                    text=match['text'],
                    location_type=match['type'].lower(),
                    confidence=95.5
                ))
