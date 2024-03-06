# coding: utf-8

"""
    Postal Mail

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.objects.postal_mail.api_client import ApiClient
from hubspot.crm.objects.postal_mail.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class BasicApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, postal_mail_id, **kwargs):  # noqa: E501
        """Archive  # noqa: E501

        Move an Object identified by `{postalMailId}` to the recycling bin.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.archive(postal_mail_id, async_req=True)
        >>> result = thread.get()

        :param postal_mail_id: (required)
        :type postal_mail_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        return self.archive_with_http_info(postal_mail_id, **kwargs)  # noqa: E501

    def archive_with_http_info(self, postal_mail_id, **kwargs):  # noqa: E501
        """Archive  # noqa: E501

        Move an Object identified by `{postalMailId}` to the recycling bin.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.archive_with_http_info(postal_mail_id, async_req=True)
        >>> result = thread.get()

        :param postal_mail_id: (required)
        :type postal_mail_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = ["postal_mail_id"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method archive" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'postal_mail_id' is set
        if self.api_client.client_side_validation and local_var_params.get("postal_mail_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `postal_mail_id` when calling `archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "postal_mail_id" in local_var_params:
            path_params["postalMailId"] = local_var_params["postal_mail_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            "/crm/v3/objects/postal_mail/{postalMailId}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )

    def create(self, simple_public_object_input_for_create, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        Create a postal mail with the given properties and return a copy of the object, including the ID. Documentation and examples for creating standard postal mail is provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(simple_public_object_input_for_create, async_req=True)
        >>> result = thread.get()

        :param simple_public_object_input_for_create: (required)
        :type simple_public_object_input_for_create: SimplePublicObjectInputForCreate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SimplePublicObject
        """
        kwargs["_return_http_data_only"] = True
        return self.create_with_http_info(simple_public_object_input_for_create, **kwargs)  # noqa: E501

    def create_with_http_info(self, simple_public_object_input_for_create, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        Create a postal mail with the given properties and return a copy of the object, including the ID. Documentation and examples for creating standard postal mail is provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_with_http_info(simple_public_object_input_for_create, async_req=True)
        >>> result = thread.get()

        :param simple_public_object_input_for_create: (required)
        :type simple_public_object_input_for_create: SimplePublicObjectInputForCreate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SimplePublicObject, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["simple_public_object_input_for_create"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method create" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'simple_public_object_input_for_create' is set
        if self.api_client.client_side_validation and local_var_params.get("simple_public_object_input_for_create") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `simple_public_object_input_for_create` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "simple_public_object_input_for_create" in local_var_params:
            body_params = local_var_params["simple_public_object_input_for_create"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            201: "SimplePublicObject",
        }

        return self.api_client.call_api(
            "/crm/v3/objects/postal_mail",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )

    def get_by_id(self, postal_mail_id, **kwargs):  # noqa: E501
        """Read  # noqa: E501

        Read an Object identified by `{postalMailId}`. `{postalMailId}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param.  Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_id(postal_mail_id, async_req=True)
        >>> result = thread.get()

        :param postal_mail_id: (required)
        :type postal_mail_id: str
        :param properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :type properties: list[str]
        :param properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :type properties_with_history: list[str]
        :param associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :type associations: list[str]
        :param archived: Whether to return only results that have been archived.
        :type archived: bool
        :param id_property: The name of a property whose values are unique for this object type
        :type id_property: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SimplePublicObjectWithAssociations
        """
        kwargs["_return_http_data_only"] = True
        return self.get_by_id_with_http_info(postal_mail_id, **kwargs)  # noqa: E501

    def get_by_id_with_http_info(self, postal_mail_id, **kwargs):  # noqa: E501
        """Read  # noqa: E501

        Read an Object identified by `{postalMailId}`. `{postalMailId}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param.  Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_id_with_http_info(postal_mail_id, async_req=True)
        >>> result = thread.get()

        :param postal_mail_id: (required)
        :type postal_mail_id: str
        :param properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :type properties: list[str]
        :param properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :type properties_with_history: list[str]
        :param associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :type associations: list[str]
        :param archived: Whether to return only results that have been archived.
        :type archived: bool
        :param id_property: The name of a property whose values are unique for this object type
        :type id_property: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SimplePublicObjectWithAssociations, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["postal_mail_id", "properties", "properties_with_history", "associations", "archived", "id_property"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_by_id" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'postal_mail_id' is set
        if self.api_client.client_side_validation and local_var_params.get("postal_mail_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `postal_mail_id` when calling `get_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "postal_mail_id" in local_var_params:
            path_params["postalMailId"] = local_var_params["postal_mail_id"]  # noqa: E501

        query_params = []
        if local_var_params.get("properties") is not None:  # noqa: E501
            query_params.append(("properties", local_var_params["properties"]))  # noqa: E501
            collection_formats["properties"] = "multi"  # noqa: E501
        if local_var_params.get("properties_with_history") is not None:  # noqa: E501
            query_params.append(("propertiesWithHistory", local_var_params["properties_with_history"]))  # noqa: E501
            collection_formats["propertiesWithHistory"] = "multi"  # noqa: E501
        if local_var_params.get("associations") is not None:  # noqa: E501
            query_params.append(("associations", local_var_params["associations"]))  # noqa: E501
            collection_formats["associations"] = "multi"  # noqa: E501
        if local_var_params.get("archived") is not None:  # noqa: E501
            query_params.append(("archived", local_var_params["archived"]))  # noqa: E501
        if local_var_params.get("id_property") is not None:  # noqa: E501
            query_params.append(("idProperty", local_var_params["id_property"]))  # noqa: E501

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "SimplePublicObjectWithAssociations",
        }

        return self.api_client.call_api(
            "/crm/v3/objects/postal_mail/{postalMailId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )

    def get_page(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        Read a page of postal mail. Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_page(async_req=True)
        >>> result = thread.get()

        :param limit: The maximum number of results to display per page.
        :type limit: int
        :param after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :type after: str
        :param properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :type properties: list[str]
        :param properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request.
        :type properties_with_history: list[str]
        :param associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :type associations: list[str]
        :param archived: Whether to return only results that have been archived.
        :type archived: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CollectionResponseSimplePublicObjectWithAssociationsForwardPaging
        """
        kwargs["_return_http_data_only"] = True
        return self.get_page_with_http_info(**kwargs)  # noqa: E501

    def get_page_with_http_info(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        Read a page of postal mail. Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_page_with_http_info(async_req=True)
        >>> result = thread.get()

        :param limit: The maximum number of results to display per page.
        :type limit: int
        :param after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :type after: str
        :param properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :type properties: list[str]
        :param properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request.
        :type properties_with_history: list[str]
        :param associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :type associations: list[str]
        :param archived: Whether to return only results that have been archived.
        :type archived: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CollectionResponseSimplePublicObjectWithAssociationsForwardPaging, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["limit", "after", "properties", "properties_with_history", "associations", "archived"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_page" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get("limit") is not None:  # noqa: E501
            query_params.append(("limit", local_var_params["limit"]))  # noqa: E501
        if local_var_params.get("after") is not None:  # noqa: E501
            query_params.append(("after", local_var_params["after"]))  # noqa: E501
        if local_var_params.get("properties") is not None:  # noqa: E501
            query_params.append(("properties", local_var_params["properties"]))  # noqa: E501
            collection_formats["properties"] = "multi"  # noqa: E501
        if local_var_params.get("properties_with_history") is not None:  # noqa: E501
            query_params.append(("propertiesWithHistory", local_var_params["properties_with_history"]))  # noqa: E501
            collection_formats["propertiesWithHistory"] = "multi"  # noqa: E501
        if local_var_params.get("associations") is not None:  # noqa: E501
            query_params.append(("associations", local_var_params["associations"]))  # noqa: E501
            collection_formats["associations"] = "multi"  # noqa: E501
        if local_var_params.get("archived") is not None:  # noqa: E501
            query_params.append(("archived", local_var_params["archived"]))  # noqa: E501

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "CollectionResponseSimplePublicObjectWithAssociationsForwardPaging",
        }

        return self.api_client.call_api(
            "/crm/v3/objects/postal_mail",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )

    def update(self, postal_mail_id, simple_public_object_input, **kwargs):  # noqa: E501
        """Update  # noqa: E501

        Perform a partial update of an Object identified by `{postalMailId}`. `{postalMailId}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param. Provided property values will be overwritten. Read-only and non-existent properties will be ignored. Properties values can be cleared by passing an empty string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update(postal_mail_id, simple_public_object_input, async_req=True)
        >>> result = thread.get()

        :param postal_mail_id: (required)
        :type postal_mail_id: str
        :param simple_public_object_input: (required)
        :type simple_public_object_input: SimplePublicObjectInput
        :param id_property: The name of a property whose values are unique for this object type
        :type id_property: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SimplePublicObject
        """
        kwargs["_return_http_data_only"] = True
        return self.update_with_http_info(postal_mail_id, simple_public_object_input, **kwargs)  # noqa: E501

    def update_with_http_info(self, postal_mail_id, simple_public_object_input, **kwargs):  # noqa: E501
        """Update  # noqa: E501

        Perform a partial update of an Object identified by `{postalMailId}`. `{postalMailId}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param. Provided property values will be overwritten. Read-only and non-existent properties will be ignored. Properties values can be cleared by passing an empty string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_with_http_info(postal_mail_id, simple_public_object_input, async_req=True)
        >>> result = thread.get()

        :param postal_mail_id: (required)
        :type postal_mail_id: str
        :param simple_public_object_input: (required)
        :type simple_public_object_input: SimplePublicObjectInput
        :param id_property: The name of a property whose values are unique for this object type
        :type id_property: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SimplePublicObject, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["postal_mail_id", "simple_public_object_input", "id_property"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method update" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'postal_mail_id' is set
        if self.api_client.client_side_validation and local_var_params.get("postal_mail_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `postal_mail_id` when calling `update`")  # noqa: E501
        # verify the required parameter 'simple_public_object_input' is set
        if self.api_client.client_side_validation and local_var_params.get("simple_public_object_input") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `simple_public_object_input` when calling `update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "postal_mail_id" in local_var_params:
            path_params["postalMailId"] = local_var_params["postal_mail_id"]  # noqa: E501

        query_params = []
        if local_var_params.get("id_property") is not None:  # noqa: E501
            query_params.append(("idProperty", local_var_params["id_property"]))  # noqa: E501

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "simple_public_object_input" in local_var_params:
            body_params = local_var_params["simple_public_object_input"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "PATCH", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "SimplePublicObject",
        }

        return self.api_client.call_api(
            "/crm/v3/objects/postal_mail/{postalMailId}",
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )
