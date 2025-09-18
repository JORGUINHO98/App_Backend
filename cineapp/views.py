from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore

from .models import Pelicula, Usuario
from .serializers import PeliculaSerializer, UsuarioSerializer


# ============================
# CRUD Película
# ============================
@api_view(['GET', 'POST'])
def peliculas(request):
    if request.method == 'GET':
        peliculas = Pelicula.objects.all()
        serializer = PeliculaSerializer(peliculas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PeliculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def pelicula_detalle(request, pk):
    try:
        pelicula = Pelicula.objects.get(pk=pk)
    except Pelicula.DoesNotExist:
        return Response({'error': 'Pelicula no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PeliculaSerializer(pelicula)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PeliculaSerializer(pelicula, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pelicula.delete()
        return Response({'mensaje': 'Pelicula eliminada correctamente'}, status=status.HTTP_204_NO_CONTENT)


# ============================
# CRUD Usuario
# ============================
@api_view(['GET', 'POST'])
def usuarios(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detalle(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response({'mensaje': 'Usuario eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)


# ============================
# Usuarios por Rol
# ============================
@api_view(['GET'])
def show_by_rol(request):
    usuarios = Usuario.objects.filter(rol_id=5, nombre='juan')
    cantidad = usuarios.count()
    serializer = UsuarioSerializer(usuarios, many=True)

    diccionario = {
        'cantidad': cantidad,
        'usuarios': serializer.data
    }
    return Response(diccionario)

# ============================
import requests # type: ignore
from django.conf import settings # type: ignore

TMDB_API_KEY = "TU_API_KEY_AQUI"  # ⚡ Reemplázalo por tu API KEY de TMDb


# ============================
# TMDb - Películas Populares
# ============================
@api_view(['GET'])
def tmdb_populares(request):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=es-ES&page=1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Devolvemos solo lo necesario
        peliculas = [
            {
                "id": movie["id"],
                "titulo": movie["title"],
                "descripcion": movie["overview"],
                "poster": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie["poster_path"] else None,
                "fecha_lanzamiento": movie["release_date"]
            }
            for movie in data.get("results", [])
        ]
        return Response(peliculas)
    else:
        return Response({"error": "No se pudo obtener la información de TMDb"}, status=status.HTTP_400_BAD_REQUEST)


# ============================
# TMDb - Buscar Película
# ============================
@api_view(['GET'])
def tmdb_buscar(request):
    query = request.GET.get("q", "")
    if not query:
        return Response({"error": "Debes enviar un parámetro ?q=nombre"}, status=status.HTTP_400_BAD_REQUEST)

    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=es-ES&query={query}&page=1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        peliculas = [
            {
                "id": movie["id"],
                "titulo": movie["title"],
                "descripcion": movie["overview"],
                "poster": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie["poster_path"] else None,
                "fecha_lanzamiento": movie["release_date"]
            }
            for movie in data.get("results", [])
        ]
        return Response(peliculas)
    else:
        return Response({"error": "No se pudo obtener la información de TMDb"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def tmdb_guardar(request):
    """
    GET -> Buscar en TMDb (con ?q=nombre)
    POST -> Guardar en BD una película de TMDb (con {tmdb_id})
    """
    if request.method == 'GET':
        query = request.GET.get("q", "")
        if not query:
            return Response({"error": "Debes enviar un parámetro ?q=nombre"}, status=status.HTTP_400_BAD_REQUEST)

        url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=es-ES&query={query}&page=1"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            peliculas = [
                {
                    "tmdb_id": movie["id"],
                    "titulo": movie["title"],
                    "descripcion": movie["overview"],
                    "poster": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie["poster_path"] else None,
                    "fecha_lanzamiento": movie["release_date"]
                }
                for movie in data.get("results", [])
            ]
            return Response(peliculas)
        else:
            return Response({"error": "No se pudo obtener la información de TMDb"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        tmdb_id = request.data.get("tmdb_id")
        if not tmdb_id:
            return Response({"error": "Debes enviar el campo tmdb_id"}, status=status.HTTP_400_BAD_REQUEST)

        # Buscar detalles en TMDb
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={TMDB_API_KEY}&language=es-ES"
        response = requests.get(url)

        if response.status_code == 200:
            movie = response.json()

            # Verificar si ya existe en BD
            if Pelicula.objects.filter(tmdb_id=movie["id"]).exists():
                return Response({"mensaje": "La película ya está guardada"}, status=status.HTTP_200_OK)

            pelicula = Pelicula.objects.create(
                tmdb_id=movie["id"],
                titulo=movie["title"],
                descripcion=movie["overview"],
                poster=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie["poster_path"] else None,
                fecha_lanzamiento=movie["release_date"] if movie["release_date"] else None
            )

            serializer = PeliculaSerializer(pelicula)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "No se pudo obtener la película en TMDb"}, status=status.HTTP_400_BAD_REQUEST)
# ============================  
# ============================
# TMDb - Guardar Favorito
# ============================
@api_view(['POST'])
def tmdb_guardar_favorito(request, usuario_id):
    """
    Guarda una película desde TMDb y la asocia como favorito a un usuario
    """
    tmdb_id = request.data.get("tmdb_id")
    if not tmdb_id:
        return Response({"error": "Debes enviar el campo tmdb_id"}, status=status.HTTP_400_BAD_REQUEST)

    # Verificar si el usuario existe
    try:
        usuario = Usuario.objects.get(pk=usuario_id)
    except Usuario.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    # Buscar detalles de la película en TMDb
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={TMDB_API_KEY}&language=es-ES"
    response = requests.get(url)

    if response.status_code == 200:
        movie = response.json()

        # Crear o recuperar película en BD
        pelicula, creada = Pelicula.objects.get_or_create(
            tmdb_id=movie["id"],
            defaults={
                "titulo": movie["title"],
                "descripcion": movie["overview"],
                "poster": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie["poster_path"] else None,
                "fecha_lanzamiento": movie["release_date"] if movie["release_date"] else None
            }
        )

        # Crear favorito si no existe
        from .models import Favorito
        favorito, fav_creado = Favorito.objects.get_or_create(
            usuario=usuario,
            id_pelicula=pelicula.id
        )

        return Response({
            "mensaje": f"La película '{pelicula.titulo}' fue agregada a favoritos de {usuario.nombre or usuario.email}",
            "pelicula": PeliculaSerializer(pelicula).data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({"error": "No se pudo obtener la película en TMDb"}, status=status.HTTP_400_BAD_REQUEST)


# ============================
# TMDb - Quitar Favorito
# ============================
@api_view(['DELETE'])
def tmdb_quitar_favorito(request, usuario_id, pelicula_id):
    """
    Quita una película de los favoritos de un usuario
    """
    try:
        usuario = Usuario.objects.get(pk=usuario_id)
    except Usuario.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    try:
        favorito = usuario.favoritos.get(id_pelicula=pelicula_id)
    except favorito.DoesNotExist:
        return Response({"mensaje": "La película no está en los favoritos de este usuario"}, status=status.HTTP_200_OK)

    favorito.delete()

    return Response({
        "mensaje": f"La película con ID {pelicula_id} fue eliminada de favoritos de {usuario.nombre or usuario.email}"
    }, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated]) # type: ignore
def update_profile(request):
    user = request.user
    data = request.data

    # actualizar nombre/email
    user.nombre = data.get("nombre", user.nombre)
    user.email = data.get("email", user.email)

    # cambiar contraseña
    password_actual = data.get("password_actual")
    password_nueva = data.get("password_nueva")
    if password_nueva and user.check_password(password_actual):
        user.set_password(password_nueva)

    user.save()
    return Response({"mensaje": "Perfil actualizado correctamente"})
