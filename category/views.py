from rest_framework import generics, status, permissions,filters
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from category.models import Category, Product, ImageProduct
from category.serializer import CategorySerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TheCategory(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','the_type']


class TheProduct(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save()


class TheProductlist(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = None

    queryset = Product.objects.prefetch_related('product')



class ProductUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()

    lookup_field = "id"



class SearchPostView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title','description']
    #
    # import youtube_dl, subprocess, random
    # from rest_framework import generics, status, permissions
    # from rest_framework.response import Response
    #
    # from convertapp.serializer import ConvertAudioSerializer
    #
    # from pydrive.auth import GoogleAuth
    # from pydrive.drive import GoogleDrive
    #
    # gauth = GoogleAuth()
    # drive = GoogleDrive(gauth)
    #
    # class ConvertAudioView(generics.GenericAPIView):
    #     serializer_class = ConvertAudioSerializer
    #
    #     def post(self, request):
    #         user = request.data
    #         serializer = self.serializer_class(data=user)
    #         serializer.is_valid(raise_exception=True)
    #         # video = user['link_video']
    #         video_url = user['link_video']
    #         video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
    #
    #         FROM = "00:00:15"
    #         TO = "00:00:25"
    #         TARGET = "demo.mp4"
    #
    #         with youtube_dl.YoutubeDL({'format': 'best'}) as ydl:
    #             result = ydl.extract_info(url=video_url, download=False)
    #             video = result['entries'][0] if 'entries' in result else result
    #
    #         url = video['url']
    #         print(url)
    #         subprocess.call('ffmpeg -i "%s" -ss %s -t %s -c:v copy -c:a copy "%s"' % (url, FROM, TO, TARGET))
    #         x = random.randint(1, 999)
    #         filename = f"{x}.mp3"
    #         options = {
    #             'format': 'bestaudio/best',
    #             'keepvideo': False,
    #             'outtmpl': filename,
    #         }
    #         with youtube_dl.YoutubeDL(options) as ydl:
    #             ydl.download([video_info['webpage_url']])
    #
    #         folder = '1IRrjYoHhUzeB0-9Jjq5bAt_DHXUpJLoF'
    #         gfile = drive.CreateFile({'parents': [{'id': folder}], 'title': filename})
    #         gfile.SetContentFile(filename)
    #         gfile.Upload()
    #         serializer.save(link=gfile.metadata['alternateLink'])
    #         return Response(data=serializer.data, status=status.HTTP_201_CREATED)




class ProductOrderUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    lookup_field = "id"
    def perform_update(self, serializer):
        order = Product.objects.get(id=self.lookup_field)
        num = order.count - self.request.data['count']
        serializer.save(count=num)
