from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, serializers
from .serializers import InsuranceDiscussionSerializers, InsuranceProductSerializers
from drf_yasg.utils import swagger_auto_schema
from .models import InsuranceDiscussion, InsuranceProduct
from django.views.generic.detail import SingleObjectMixin

import logging
import sys

# Get an instance of a logger
logger = logging.getLogger(__name__)

class InsuranceDiscussionAPI(APIView):
    """
        Retrieve, update or delete a InsuranceDiscussion i.
    """
    def response(self, data=None, success=True, **message):
        if data and success:
            return Response(data={"result": "success", "data": data},
                            status=status.HTTP_200_OK)
        elif success:
            return Response(data={"result": "success"},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={"result": "failed", "message": message.get("err", "UNKNOWN ERROR")},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if request.request.GET['id']:
            insurance_discussions = InsuranceDiscussion.objects.filter(id=request.GET['id']).values()
        else:
            insurance_discussions = InsuranceDiscussion.objects.all().values()
        if insurance_discussions:
            self.response(data=insurance_discussions)
        else:
            self.response(success=False, err='No data found')


    def post(self, request):
        serializer = InsuranceDiscussionSerializers(data=request.data)
        if serializer.is_valid():
            save_rec = serializer.save()
            self.response(data=[{'record_id': save_rec}])
        else:
            self.response(success=False, err=serializer.errors)


    def put(self, request):
        dis = InsuranceDiscussion.objects.get(id=request.GET['id'])
        serializer = InsuranceDiscussionSerializers(instance=dis, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            self.response(data=serializer.validated_data)
        else:
            self.response(success=False, err=serializer.errors)


    def delete(self, request):
        insurance_discussion = InsuranceDiscussion.objects.filter(id=request.GET['id'])
        if insurance_discussion:
            insurance_discussion.delete()
            self.response()
        else:
            self.response(success=False, err="No data found")




class InsuranceDiscussionCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(query_serializer=InsuranceDiscussionSerializers)
    def post(self, request):
        serializer = InsuranceDiscussionSerializers(data=request.data)
        if serializer.is_valid():
            save_rec = serializer.save()
            return Response(data={"result": "success", "record_id": save_rec.id},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={"result": "error", "data": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class InsuranceDiscussionList(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(query_serializer=InsuranceDiscussionSerializers)
    def get(self, request):
        insurance_discussions = InsuranceDiscussion.objects.all().values()
        serializer = InsuranceDiscussionSerializers(insurance_discussions, many=True)
        if insurance_discussions:
            return Response(data={"result": "success", "data": insurance_discussions},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={"result": "No data found"},
                            status=status.HTTP_400_BAD_REQUEST)


class InsuranceDiscussionGet(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(query_serializer=InsuranceDiscussionSerializers)
    def get(self, request):
        insurance_discussion = InsuranceDiscussion.objects.filter(id=request.GET['id']).values()
        serializer = InsuranceDiscussionSerializers(insurance_discussion, many=True)
        if insurance_discussion:
            return Response(data={"result": "success", "data": insurance_discussion},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={"result": "No data found"},
                            status=status.HTTP_400_BAD_REQUEST)


class InsuranceDiscussionDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(query_serializer=InsuranceDiscussionSerializers)
    def delete(self, request):
        insurance_discussion = InsuranceDiscussion.objects.filter(id=request.GET['id'])
        if insurance_discussion:
            insurance_discussion.delete()
            return Response(data={"result": "success"},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={"result": "No data found"},
                            status=status.HTTP_400_BAD_REQUEST)


class InsuranceDiscussionUpdate(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(query_serializer=InsuranceDiscussionSerializers)
    def put(self, request):
        dis = InsuranceDiscussion.objects.get(id=request.GET['id'])
        serializer = InsuranceDiscussionSerializers(instance=dis, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"result": "success", "data": serializer.validated_data},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={"result": "No data found"},
                            status=status.HTTP_400_BAD_REQUEST)

