from django.contrib import admin
from django.utils.html import format_html

from network.models import ContactsFactory, Network, ProductsFactory


@admin.register(ContactsFactory)
class ContactsFactoryAdmin(admin.ModelAdmin):
    list_display = ("email_cont", "number_phone_cont", "country_cont", "city_cont")


@admin.action(description="Очистить задолженность")
def make_published(modeladmin, request, queryset):
    queryset.update(debt_fact=0)


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):

    def get_city(self, obj):
        """Получаем город из связанной модели ContactsFactory"""
        if obj.contacts_fact:  # используем правильное имя поля contacts_fact
            return obj.contacts_fact.city_cont
        return "Нет города"

    get_city.short_description = "Город"

    def supplier_link(self, obj):
        if obj.supplier_fact:
            return format_html(
                '<a href="/admin/network/network/{}/change/">{}</a>',
                obj.supplier_fact.id,
                obj.supplier_fact.name_fact,
            )
        return "Нет поставщика"

    supplier_link.short_description = "Поставщик"  # Кликабельная ссылка

    list_display = ["debt_fact", "level", "supplier_link", "get_city"]
    list_filter = ("contacts_fact__city_cont",)
    actions = [make_published]


@admin.register(ProductsFactory)
class ProductsFactoryAdmin(admin.ModelAdmin):
    list_display = ("name_pr", "models_pr", "release_pr")
