from .serializer import *
from .filters import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .pagination import CustomPagination
from rest_framework.response import Response
from rest_framework import status


class ClientListAPIView(generics.ListAPIView):
    serializer_class = ClientViewSerializer

    def get_queryset(self):
        queryset = Client.objects.get_queryset()
        params = self.request.query_params

        legal_entity = params.get('legal_entity', None)

        if legal_entity:
            queryset = queryset.filter(legal_entity=legal_entity)

        return queryset


class ClientCreateAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer


class ClientRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientViewSerializer


class ServicesPLListAPIView(generics.ListAPIView):
    serializer_class = ServicesPLWTypeViewSerializer

    def get_queryset(self):
        queryset = ServicesPL.objects.all()
        params = self.request.query_params

        service_type = params.get('service_type', None)

        if service_type:
            queryset = queryset.filter(service_type=service_type)

        return queryset


class ServicesPLCreateAPIView(generics.CreateAPIView):
    queryset = ServicesPL.objects.all()
    serializer_class = ServicesPLCreateSerializer


class ServicesPLRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicesPL.objects.all()
    serializer_class = ServicesPLViewSerializer


class MaterialsPLListAPIView(generics.ListAPIView):
    queryset = MaterialsPL.objects.all()
    serializer_class = MaterialsPLViewSerializer


class MaterialsPLCreateAPIView(generics.CreateAPIView):
    queryset = MaterialsPL.objects.all()
    serializer_class = MaterialsPLCreateSerializer


class MaterialsPLRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaterialsPL.objects.all()
    serializer_class = MaterialsPLViewSerializer


class RequestListAPIView(generics.ListAPIView):
    serializer_class = RequestWStatusViewSerializer

    def get_queryset(self):
        queryset = Request.objects.all()
        params = self.request.query_params

        status = params.get('status', None)
        from_date = params.get('from_date', None)
        to_date = params.get('to_date', None)
        legal_entity = params.get('legal_entity', None)

        if status:
            queryset = queryset.filter(status=status)

        if from_date:
            queryset = queryset.filter(req_date__gte=from_date)

        if to_date:
            queryset = queryset.filter(req_date__lte=to_date)

        if legal_entity:
            queryset = queryset.filter(client__legal_entity=legal_entity)

        return queryset


class RequestCreateAPIView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestCreateSerializer


class RequestRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestViewSerializer


class RequestNestedAPIView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestNestedSerializer


class ChosenServicesListAPIView(generics.ListAPIView):
    serializer_class = ChosenServicesWSRViewSerializer

    def get_queryset(self):
        queryset = ChosenServices.objects.all()
        params = self.request.query_params

        req = params.get('req', None)

        if req:
            queryset = queryset.filter(req=req)

        return queryset


class ChosenServicesCreateAPIView(generics.CreateAPIView):
    queryset = ChosenServices.objects.all()
    serializer_class = ChosenServicesCreateSerializer


class ChosenServicesRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChosenServices.objects.all()
    serializer_class = ChosenServicesViewSerializer


class ChosenServicesFullListAPIView(generics.ListAPIView):
    queryset = ChosenServices.objects.all()
    serializer_class = ChosenServicesNestedSerializer


class ChosenMaterialsListAPIView(generics.ListAPIView):
    serializer_class = ChosenMaterialWMRsViewSerializer

    def get_queryset(self):
        queryset = ChosenMaterials.objects.all()
        params = self.request.query_params

        req = params.get('req', None)

        if req:
            queryset = queryset.filter(req=req)

        return queryset


class ChosenMaterialsCreateAPIView(generics.CreateAPIView):
    queryset = ChosenMaterials.objects.all()
    serializer_class = ChosenMaterialsCreateSerializer


class ChosenMaterialsRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChosenMaterials.objects.all()
    serializer_class = ChosenMaterialsViewSerializer


class ChosenMaterialsFullListAPIView(generics.ListAPIView):
    queryset = ChosenMaterials.objects.all()
    serializer_class = ChosenMaterialsNestedSerializer


class WorkGroupListAPIView(generics.ListAPIView):
    serializer_class = WorkGroupWREViewSerializer

    def get_queryset(self):
        queryset = WorkGroup.objects.all()
        params = self.request.query_params

        req = params.get('req', None)
        executor = params.get('executor', None)
        start_date = params.get('start_date', None)
        end_date = params.get('end_date', None)

        if req:
            queryset = queryset.filter(req=req)

        if executor:
            queryset = queryset.filter(executor=executor)

        if start_date:
            queryset = queryset.filter(start_date__gte=start_date)

        if end_date:
            queryset = queryset.filter(end_date__lte=end_date)

        return queryset


class WorkGroupCreateAPIView(generics.CreateAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = WorkGroupCreateSerializer


class WorkGroupRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = WorkGroupViewSerializer


class WorkGroupFullListAPIView(generics.ListAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = WorkGroupNestedSerializer


class ExecutorListAPIView(generics.ListAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorViewSerializer


class ExecutorCreateAPIView(generics.CreateAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorCreateSerializer


class ExecutorRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorViewSerializer


class InvoiceListAPIView(generics.ListAPIView):
    serializer_class = InvoiceViewNestedSerializer

    def get_queryset(self):
        queryset = Invoice.objects.all()
        params = self.request.query_params

        legal_entity = params.get('legal_entity', None)

        if legal_entity:
            queryset = queryset.filter(client__legal_entity=legal_entity)

        return queryset


class InvoiceCreateAPIView(generics.CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceCreateSerializer


class InvoiceRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceViewSerializer


class PaymentOrderListAPIView(generics.ListAPIView):
    queryset = PaymentOrder.objects.all()
    serializer_class = PaymentOrderNestedSerializer


class PaymentOrderCreateAPIView(generics.CreateAPIView):
    queryset = PaymentOrder.objects.all()
    serializer_class = PaymentOrderCreateSerializer


class PaymentOrderRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentOrder.objects.all()
    serializer_class = PaymentOrderViewSerializer


# кастомная пагинация
# ручной фильтр - принимает 1 параметр
class ClientFilterView(generics.ListAPIView):
    serializer_class = ClientViewSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Client.objects.all()
        legal_entity = self.request.query_params.get('legal_entity')
        if legal_entity:
            queryset = queryset.filter(legal_entity=legal_entity)
        return queryset


# ручной фильтр - принимает 2 параметра
class ServicesPLFilterView(generics.ListAPIView):
    serializer_class = ServicesPLViewSerializer

    def get_queryset(self):
        queryset = ServicesPL.objects.all()
        service_type = self.request.query_params.get('service_type')
        price = self.request.query_params.get('price')
        if service_type:
            queryset = queryset.filter(service_type=service_type)
        if price:
            queryset = queryset.filter(price=price)
        return queryset


# ручной фильтр - отфильтрованные данные только если пользователь авторизован
class RequestFilterView(generics.ListAPIView):
    serializer_class = RequestViewSerializer

    def get_queryset(self):
        queryset = Request.objects.all()
        if self.request.user.is_authenticated:
            status = self.request.query_params.get('status')
            final_price = self.request.query_params.get('final_price')
            if status:
                queryset = queryset.filter(status=status)
            if final_price:
                queryset = queryset.filter(final_price=final_price)
        return queryset


# автоматический фильтр - сортировка по дате
class WorkGroupFilterView(generics.ListAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = WorkGroupViewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['start_date']


# автоматический фильтр - поиск
class ExecutorSearchFilterView(generics.ListAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorViewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['full_name', 'phone_num']


# автоматический фильтр - поиск по полям из связной таблицы
class InvoiceSearchFilterView(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceViewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['client__contact_person']


# автоматический фильтр - сортировка в диапазоне количества
class ChosenMaterialsRangeFilterView(generics.ListAPIView):
    queryset = ChosenMaterials.objects.all()
    serializer_class = ChosenMaterialsViewSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ChosenMaterialsRangeFilter


class MaterialsPhotoAPIView(generics.CreateAPIView):
    queryset = MaterialsPhoto.objects.all()
    serializer_class = MaterialsPhotoSerializer


class MaterialsPhotosAPIView(generics.CreateAPIView):
    queryset = MaterialsPhoto.objects.all()
    serializer_class = MaterialsPhotoSerializer

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')
        for file in files:
            file_instance = MaterialsPhoto(material=MaterialsPL.objects.get(
                id=request.POST.get('material')), file=file)
            file_instance.save()
        return Response(request.data, status=status.HTTP_201_CREATED)
