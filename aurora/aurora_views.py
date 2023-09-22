from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required 


@login_required(login_url='aurora:login')
def index(request):
    context={
        "page_title":"Dashboard"
    }
    return render(request,'aurora/index.html',context)

@login_required(login_url='aurora:login')
def index2(request):
    context={
        "page_title":"Dashboard"
    }
    return render(request,'aurora/index-2.html',context)

@login_required(login_url='aurora:login')
def my_wallet(request):
    context={
        "page_title":"My Wallet"
    }
    return render(request,'aurora/my-wallet.html',context)

@login_required(login_url='aurora:login')
def invoices(request):
    context={
        "page_title":"Invoices"
    }
    return render(request,'aurora/invoices.html',context)

@login_required(login_url='aurora:login')
def cards_center(request):
    context={
        "page_title":"Cards Center"
    }
    return render(request,'aurora/cards-center.html',context)

@login_required(login_url='aurora:login')
def transactions(request):
    context={
        "page_title":"Transactions"
    }
    return render(request,'aurora/transactions.html',context)


@login_required(login_url='aurora:login')
def transactions_details(request):
    context={
        "page_title":"Transactions Details"
    }
    return render(request,'aurora/transactions-details.html',context)



@login_required(login_url='aurora:login')
def app_profile(request):
    context={
        "page_title":"Profile"
    }
    return render(request,'aurora/apps/app-profile.html',context)


@login_required(login_url='aurora:login')
def post_details(request):
    context={
        "page_title":"Post Details"
    }
    return render(request,'aurora/apps/post-details.html',context)

@login_required(login_url='aurora:login')
def email_compose(request):
    context={
        "page_title":"Compose"
    }
    return render(request,'aurora/apps/email/email-compose.html',context)

@login_required(login_url='aurora:login')
def email_inbox(request):
    context={
        "page_title":"Inbox"
    }
    return render(request,'aurora/apps/email/email-inbox.html',context)

@login_required(login_url='aurora:login')
def email_read(request):
    context={
        "page_title":"Read"
    }
    return render(request,'aurora/apps/email/email-read.html',context)

@login_required(login_url='aurora:login')
def app_calender(request):
    context={
        "page_title":"Calendar"
    }
    return render(request,'aurora/apps/app-calender.html',context)


@login_required(login_url='aurora:login')
def ecom_product_grid(request):
    context={
        "page_title":"Product-Grid"
    }
    return render(request,'aurora/apps/shop/ecom-product-grid.html',context)

@login_required(login_url='aurora:login')
def ecom_product_list(request):
    context={
        "page_title":"Product-List"
    }
    return render(request,'aurora/apps/shop/ecom-product-list.html',context)

@login_required(login_url='aurora:login')
def ecom_product_detail(request):
    context={
        "page_title":"Product-Detail"
    }
    return render(request,'aurora/apps/shop/ecom-product-detail.html',context)

@login_required(login_url='aurora:login')
def ecom_product_order(request):
    context={
        "page_title":"Product-Order"
    }
    return render(request,'aurora/apps/shop/ecom-product-order.html',context)

@login_required(login_url='aurora:login')
def ecom_checkout(request):
    context={
        "page_title":"Checkout"
    }
    return render(request,'aurora/apps/shop/ecom-checkout.html',context)

@login_required(login_url='aurora:login')
def ecom_invoice(request):
    context={
        "page_title":"Invoice"
    }
    return render(request,'aurora/apps/shop/ecom-invoice.html',context)

@login_required(login_url='aurora:login')
def ecom_customers(request):
    context={
        "page_title":"Customers"
    }
    return render(request,'aurora/apps/shop/ecom-customers.html',context)


@login_required(login_url='aurora:login')
def chart_flot(request):
    context={
        "page_title":"Chart-Flot"
    }
    return render(request,'aurora/charts/chart-flot.html',context)

@login_required(login_url='aurora:login')
def chart_morris(request):
    context={
        "page_title":"Chart-Morris"
    }
    return render(request,'aurora/charts/chart-morris.html',context)

@login_required(login_url='aurora:login')
def chart_chartjs(request):
    context={
        "page_title":"Chart-Chartjs"
    }
    return render(request,'aurora/charts/chart-chartjs.html',context)

@login_required(login_url='aurora:login')
def chart_chartist(request):
    context={
        "page_title":"Chart-Chartist"
    }
    return render(request,'aurora/charts/chart-chartist.html',context)

@login_required(login_url='aurora:login')
def chart_sparkline(request):
    context={
        "page_title":"Chart-Sparkline"
    }
    return render(request,'aurora/charts/chart-sparkline.html',context)

@login_required(login_url='aurora:login')
def chart_peity(request):
    context={
        "page_title":"Chart-Peity"
    }
    return render(request,'aurora/charts/chart-peity.html',context)



@login_required(login_url='aurora:login')
def ui_accordion(request):
    context={
        "page_title":"Accordion"
    }
    return render(request,'aurora/bootstrap/ui-accordion.html',context)

@login_required(login_url='aurora:login')
def ui_alert(request):
    context={
        "page_title":"Alert"
    }
    return render(request,'aurora/bootstrap/ui-alert.html',context)

@login_required(login_url='aurora:login')
def ui_badge(request):
    context={
        "page_title":"Badge"
    }
    return render(request,'aurora/bootstrap/ui-badge.html',context)

@login_required(login_url='aurora:login')
def ui_button(request):
    context={
        "page_title":"Button"
    }
    return render(request,'aurora/bootstrap/ui-button.html',context)

@login_required(login_url='aurora:login')
def ui_modal(request):
    context={
        "page_title":"Modal"
    }
    return render(request,'aurora/bootstrap/ui-modal.html',context)

@login_required(login_url='aurora:login')
def ui_button_group(request):
    context={
        "page_title":"Button Group"
    }
    return render(request,'aurora/bootstrap/ui-button-group.html',context)

@login_required(login_url='aurora:login')
def ui_list_group(request):
    context={
        "page_title":"List Group"
    }
    return render(request,'aurora/bootstrap/ui-list-group.html',context)

@login_required(login_url='aurora:login')
def ui_media_object(request):
    context={
        "page_title":"Media Object"
    }
    return render(request,'aurora/bootstrap/ui-media-object.html',context)


@login_required(login_url='aurora:login')
def ui_card(request):
    context={
        "page_title":"Card"
    }
    return render(request,'aurora/bootstrap/ui-card.html',context)


@login_required(login_url='aurora:login')
def ui_carousel(request):
    context={
        "page_title":"Carousel"
    }
    return render(request,'aurora/bootstrap/ui-carousel.html',context)


@login_required(login_url='aurora:login')
def ui_dropdown(request):
    context={
        "page_title":"Dropdown"
    }
    return render(request,'aurora/bootstrap/ui-dropdown.html',context)

@login_required(login_url='aurora:login')
def ui_popover(request):
    context={
        "page_title":"Popover"
    }
    return render(request,'aurora/bootstrap/ui-popover.html',context)

@login_required(login_url='aurora:login')
def ui_progressbar(request):
    context={
        "page_title":"Progressbar"
    }
    return render(request,'aurora/bootstrap/ui-progressbar.html',context)

@login_required(login_url='aurora:login')
def ui_tab(request):
    context={
        "page_title":"Tab"
    }
    return render(request,'aurora/bootstrap/ui-tab.html',context)

@login_required(login_url='aurora:login')
def ui_typography(request):
    context={
        "page_title":"Typography"
    }
    return render(request,'aurora/bootstrap/ui-typography.html',context)


@login_required(login_url='aurora:login')
def ui_pagination(request):
    context={
        "page_title":"Pagination"
    }
    return render(request,'aurora/bootstrap/ui-pagination.html',context)
@login_required(login_url='aurora:login')
def ui_grid(request):
    context={
        "page_title":"Grid"
    }
    return render(request,'aurora/bootstrap/ui-grid.html',context)




@login_required(login_url='aurora:login')
def uc_select2(request):
    context={
        "page_title":"Select"
    }
    return render(request,'aurora/plugins/uc-select2.html',context)

@login_required(login_url='aurora:login')
def uc_nestable(request):
    context={
        "page_title":"Nestable"
    }
    return render(request,'aurora/plugins/uc-nestable.html',context)

@login_required(login_url='aurora:login')
def uc_noui_slider(request):
    context={
        "page_title":"UI Slider"
    }
    return render(request,'aurora/plugins/uc-noui-slider.html',context)


@login_required(login_url='aurora:login')
def uc_sweetalert(request):
    context={
        "page_title":"Sweet Alert"
    }
    return render(request,'aurora/plugins/uc-sweetalert.html',context)

@login_required(login_url='aurora:login')
def uc_toastr(request):
    context={
        "page_title":"Toastr"
    }
    return render(request,'aurora/plugins/uc-toastr.html',context)

@login_required(login_url='aurora:login')
def map_jqvmap(request):
    context={
        "page_title":"Jqvmap"
    }
    return render(request,'aurora/plugins/map-jqvmap.html',context)

@login_required(login_url='aurora:login')
def uc_lightgallery(request):
    context={
        "page_title":"LightGallery"
    }
    return render(request,'aurora/plugins/uc-lightgallery.html',context)

@login_required(login_url='aurora:login')
def widget_basic(request):
    context={
        "page_title":"Widget"
    }
    return render(request,'aurora/widget-basic.html',context)

@login_required(login_url='aurora:login')
def form_element(request):
    context={
        "page_title":"Form Element"
    }
    return render(request,'aurora/forms/form-element.html',context)

@login_required(login_url='aurora:login')
def form_wizard(request):
    context={
        "page_title":"Form Wizard"
    }
    return render(request,'aurora/forms/form-wizard.html',context)

@login_required(login_url='aurora:login')
def form_ckeditor(request):
    context={
        "page_title":"Ckeditor"
    }
    return render(request,'aurora/forms/form-ckeditor.html',context)

@login_required(login_url='aurora:login')
def form_pickers(request):
    context={
        "page_title":"Pickers"
    }
    return render(request,'aurora/forms/form-pickers.html',context)


@login_required(login_url='aurora:login')
def form_validation_jquery(request):
    context={
        "page_title":"Form Validation"
    }
    return render(request,'aurora/forms/form-validation-jquery.html',context)


@login_required(login_url='aurora:login')
def table_bootstrap_basic(request):
    context={
        "page_title":"Table Bootstrap"
    }
    return render(request,'aurora/table/table-bootstrap-basic.html',context)

@login_required(login_url='aurora:login')
def table_datatable_basic(request):
    context={
        "page_title":"Table Datatable"
    }
    return render(request,'aurora/table/table-datatable-basic.html',context)


@login_required(login_url='aurora:login')
def page_login(request):
    return render(request,'aurora/pages/page-login.html')


@login_required(login_url='aurora:login')
def page_register(request):
    return render(request,'aurora/pages/page-register.html')


@login_required(login_url='aurora:login')
def page_lock_screen(request):
    return render(request,'aurora/pages/page-lock-screen.html')


@login_required(login_url='aurora:login')
def page_forgot_password(request):
    return render(request,'aurora/pages/page-forgot-password.html')


def page_error_400(request):
    return render(request,'400.html')
    
def page_error_403(request):
    return render(request,'403.html')

def page_error_404(request):
    return render(request,'404.html')

def page_error_500(request):
    return render(request,'500.html')

def page_error_503(request):
    return render(request,'503.html')


