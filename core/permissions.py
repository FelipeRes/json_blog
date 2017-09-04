from rest_framework import permissions

class IsUserOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return ((request.method in permissions.SAFE_METHODS) or (obj == request.user))

class IsPostOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return ((request.method in permissions.SAFE_METHODS) or (obj.perfil.user == request.user))

class IsCommentOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return ((request.method in permissions.SAFE_METHODS) or (obj.post.perfil.user == request.user))

class IsPerfilOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return ((request.method in permissions.SAFE_METHODS) or (obj.user == request.user))