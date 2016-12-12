from rest_framework import viewsets, status, response
from fcm.utils import get_device_model
from fcm.serializers import DeviceSerializer
Device = get_device_model()


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def create(self, request, *args, **kwargs):
        try:
            device = Device.objects.get(dev_id=request.data.get("dev_id"))
            serializer = self.get_serializer(device, data=request.data)
        except Device.DoesNotExist:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(is_active=True)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = Device.objects.get(dev_id=kwargs["pk"])
            self.perform_destroy(instance)
            return response.Response(status=status.HTTP_200_OK)
        except Device.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
