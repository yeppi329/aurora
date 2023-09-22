from django.urls import path
from aurora import aurora_views
from users import users_views

app_name = "aurora"

urlpatterns = [

    path("", aurora_views.index, name="index"),
    path("index/", aurora_views.index, name="index"),

    path("login/", users_views.login_user, name="login"),
    path("logout/", users_views.logout_user, name="logout"),
    path("signup/", users_views.signup, name="signup"),
    path("activate/<uidb64>/<token>/", users_views.activate, name="activate"),

    path("users/", users_views.users, name="users"),
    path("user-details/<int:id>/", users_views.user_details, name="user-details"),
    path("add-user/", users_views.add_user, name="add-user"),
    path("edit-user/<int:id>/", users_views.edit_user, name="edit-user"),
    path("delete-user/<int:id>/", users_views.delete_user, name="delete-user"),

    path("groups/", users_views.groups_list, name="groups"),
    path("group-edit/<int:id>/", users_views.group_edit, name="group-edit"),
    path("group-delete/<int:id>/", users_views.group_delete, name="group-delete"),
    path("group-add/", users_views.group_add, name="group-add"),

    path("permissions/", users_views.permissions, name="permissions"),
    path(
        "edit-permissions/<int:id>/",
        users_views.edit_permissions,
        name="edit-permissions",
    ),
    path(
        "delete-permissions/<int:id>/",
        users_views.delete_permissions,
        name="delete-permissions",
    ),
    path(
        "assign-permissions-to-user/<int:id>/",
        users_views.assign_permissions_to_user,
        name="assign-permissions-to-user",
    ),

    path("data/svc-user-status/", aurora_views.svc_user_status, name="svc-user-status"),
    path("data/scan-status/", aurora_views.scan_status, name="scan-status"),

    path(
        "operation/svc-user-list/",
        aurora_views.svc_user_list,
        name="svc-user-list",
    ),
    path(
        "operation/object-list/",
        aurora_views.object_list,
        name="object-list",
    ),
    path(
        "operation/content-list/",
        aurora_views.content_list,
        name="content-list",
    ),
    path(
        "operation/report-list/",
        aurora_views.report_list,
        name="report-list",
    ),

    path("invoices/", aurora_views.invoices, name="invoices"),
    path("index-2/", aurora_views.index2, name="index-2"),
    path("my-wallet/", aurora_views.my_wallet, name="my-wallet"),
    path("cards-center/", aurora_views.cards_center, name="cards-center"),
    path("transactions/", aurora_views.transactions, name="transactions"),
    path(
        "transactions-details/",
        aurora_views.transactions_details,
        name="transactions-details",
    ),
    path("app-profile/", aurora_views.app_profile, name="app-profile"),
    path("post-details/", aurora_views.post_details, name="post-details"),
    path("email-compose/", aurora_views.email_compose, name="email-compose"),
    path("email-inbox/", aurora_views.email_inbox, name="email-inbox"),
    path("email-read/", aurora_views.email_read, name="email-read"),
    path("app-calender/", aurora_views.app_calender, name="app-calender"),
    path(
        "ecom-product-grid/", aurora_views.ecom_product_grid, name="ecom-product-grid"
    ),
    path(
        "ecom-product-list/", aurora_views.ecom_product_list, name="ecom-product-list"
    ),
    path(
        "ecom-product-detail/",
        aurora_views.ecom_product_detail,
        name="ecom-product-detail",
    ),
    path(
        "ecom-product-order/",
        aurora_views.ecom_product_order,
        name="ecom-product-order",
    ),
    path("ecom-checkout/", aurora_views.ecom_checkout, name="ecom-checkout"),
    path("ecom-invoice/", aurora_views.ecom_invoice, name="ecom-invoice"),
    path("ecom-customers/", aurora_views.ecom_customers, name="ecom-customers"),
    path("chart-flot/", aurora_views.chart_flot, name="chart-flot"),
    path("chart-morris/", aurora_views.chart_morris, name="chart-morris"),
    path("chart-chartjs/", aurora_views.chart_chartjs, name="chart-chartjs"),
    path("chart-chartist/", aurora_views.chart_chartist, name="chart-chartist"),
    path("chart-sparkline/", aurora_views.chart_sparkline, name="chart-sparkline"),
    path("chart-peity/", aurora_views.chart_peity, name="chart-peity"),
    path("ui-accordion/", aurora_views.ui_accordion, name="ui-accordion"),
    path("ui-alert/", aurora_views.ui_alert, name="ui-alert"),
    path("ui-badge/", aurora_views.ui_badge, name="ui-badge"),
    path("ui-button/", aurora_views.ui_button, name="ui-button"),
    path("ui-modal/", aurora_views.ui_modal, name="ui-modal"),
    path("ui-button-group/", aurora_views.ui_button_group, name="ui-button-group"),
    path("ui-list-group/", aurora_views.ui_list_group, name="ui-list-group"),
    path("ui-media-object/", aurora_views.ui_media_object, name="ui-media-object"),
    path("ui-card/", aurora_views.ui_card, name="ui-card"),
    path("ui-carousel/", aurora_views.ui_carousel, name="ui-carousel"),
    path("ui-dropdown/", aurora_views.ui_dropdown, name="ui-dropdown"),
    path("ui-popover/", aurora_views.ui_popover, name="ui-popover"),
    path("ui-progressbar/", aurora_views.ui_progressbar, name="ui-progressbar"),
    path("ui-tab/", aurora_views.ui_tab, name="ui-tab"),
    path("ui-typography/", aurora_views.ui_typography, name="ui-typography"),
    path("ui-pagination/", aurora_views.ui_pagination, name="ui-pagination"),
    path("ui-grid/", aurora_views.ui_grid, name="ui-grid"),
    path("uc-select2/", aurora_views.uc_select2, name="uc-select2"),
    path("uc-nestable/", aurora_views.uc_nestable, name="uc-nestable"),
    path("uc-noui-slider/", aurora_views.uc_noui_slider, name="uc-noui-slider"),
    path("uc-sweetalert/", aurora_views.uc_sweetalert, name="uc-sweetalert"),
    path("uc-toastr/", aurora_views.uc_toastr, name="uc-toastr"),
    path("map-jqvmap/", aurora_views.map_jqvmap, name="map-jqvmap"),
    path("uc-lightgallery/", aurora_views.uc_lightgallery, name="uc-lightgallery"),
    path("uc-lightgallery/", aurora_views.uc_lightgallery, name="uc-lightgallery"),
    path("widget-basic/", aurora_views.widget_basic, name="widget-basic"),
    path("form-element/", aurora_views.form_element, name="form-element"),
    path("form-wizard/", aurora_views.form_wizard, name="form-wizard"),
    path("form-ckeditor/", aurora_views.form_ckeditor, name="form-ckeditor"),
    path("form-pickers/", aurora_views.form_pickers, name="form-pickers"),
    path(
        "form-validation-jquery/",
        aurora_views.form_validation_jquery,
        name="form-validation-jquery",
    ),
    path(
        "table-bootstrap-basic/",
        aurora_views.table_bootstrap_basic,
        name="table-bootstrap-basic",
    ),
    path(
        "table-datatable-basic/",
        aurora_views.table_datatable_basic,
        name="table-datatable-basic",
    ),
    path("page-login/", aurora_views.page_login, name="page-login"),
    path("page-register/", aurora_views.page_register, name="page-register"),
    path(
        "page-forgot-password/",
        aurora_views.page_forgot_password,
        name="page-forgot-password",
    ),
    path("page-lock-screen/", aurora_views.page_lock_screen, name="page-lock-screen"),
    path("page-error-400/", aurora_views.page_error_400, name="page-error-400"),
    path("page-error-403/", aurora_views.page_error_403, name="page-error-403"),
    path("page-error-404/", aurora_views.page_error_404, name="page-error-404"),
    path("page-error-500/", aurora_views.page_error_500, name="page-error-500"),
    path("page-error-503/", aurora_views.page_error_503, name="page-error-503"),
]
