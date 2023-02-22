from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from data.models import Data as DataModel
from data.serializers import DataSerializer

class DataTestView(APIView):
    def get(self, request):

        data_obj_list = DataModel.objects.all()

        return Response(DataSerializer(data_obj_list, many=True).data, status=status.HTTP_200_OK)
    

    def post(self, request):

        data_info_list = request.data

        data_obj_list = []
        for data_info in data_info_list:
            data_obj = DataModel(**data_info)
            data_obj_list.append(data_obj)

        data_obj_list = DataModel.objects.bulk_create(data_obj_list)

        return Response(DataSerializer(data_obj_list, many=True).data, status=status.HTTP_200_OK)
    

    def put(self, request):

        data_info_list = request.data

        data_info_dict = {}
        data_id_list = []

        for data_info in data_info_list:
            data_info_dict[data_info["id"]] = data_info
            data_id_list.append(data_info["id"])
            
        data_obj_list = DataModel.objects.filter(id__in=data_id_list)
        # data_obj_dict = {data_obj.id : data_obj for data_obj in data_obj_list}
        
        # for data_info in data_info_list:
        #     data_obj_dict[data_info["id"]].name = data_info["name"]
        #     data_obj_dict[data_info["id"]].data_no = data_info["data_no"]

        # DataModel.objects.bulk_update(data_obj_list, fields=["name", "data_no"])

        bulk_update_fields = []
        for data_obj in data_obj_list:
            data_info = data_info_dict[data_obj.id]
            
            update_fields = data_info.keys()
            data_fields = data_obj.__dict__.keys()

            for data_field in data_fields:
                if data_field == "id":
                    continue

                if data_field not in update_fields:
                    continue

                setattr(data_obj, data_field, data_info[data_field])
                bulk_update_fields.append(data_field)

        DataModel.objects.bulk_update(data_obj_list, fields=bulk_update_fields)

        data_obj_list = DataModel.objects.all()

        return Response(DataSerializer(data_obj_list, many=True).data, status=status.HTTP_200_OK)
    

    def delete(self, request):

        

        return Response({}, status=status.HTTP_200_OK)
    
    
