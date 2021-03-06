from rest_framework.permissions import BasePermission
from timeline.decorator import decorator_api
from django.conf import settings
__all__ = [
    "KeyAPIRequiredMixin", "KeyListRequiredMixin", "KeyCreateRequiredMixin",
    "KeyUpdateRequiredMixin", "KeyDeleteRequiredMixin"
]


class KeyAPIRequiredMixin(BasePermission):
    def has_permission(self, request, view):
        perms = self.permission_required
        perm_list=list(request.user.get_all_permissions())
        if request.user.is_superuser:
            return True
        if perms in perm_list:
            return True
        else:
            return False


class KeyListRequiredMixin(KeyAPIRequiredMixin):
    permission_required = u'authority.yo_list_key'


class KeyCreateRequiredMixin(KeyAPIRequiredMixin):
    permission_required = u'authority.yo_create_key'

    @decorator_api(settings.TIMELINE_KEY_CREATE)
    def has_permission(self, request, view):
        return request, super(KeyCreateRequiredMixin, self).has_permission(request, view)


class KeyUpdateRequiredMixin(KeyAPIRequiredMixin):
    permission_required = u'authority.yo_update_key'

    @decorator_api(settings.TIMELINE_KEY_UPDATE)
    def has_permission(self, request, view):
        return request, super(KeyUpdateRequiredMixin, self).has_permission(request, view)


class KeyDeleteRequiredMixin(KeyAPIRequiredMixin):
    permission_required = u'authority.yo_delete_key'

    @decorator_api(settings.TIMELINE_KEY_DELETE)
    def has_permission(self, request, view):
        return request, super(KeyDeleteRequiredMixin, self).has_permission(request, view)