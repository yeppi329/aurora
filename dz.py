# Static Folder Name
folderName = "aurora"

dz_array = {
    "public": {
        "favicon": f"{folderName}/images/favicon.png",
        "description": "aurora : Arbeon Admin Dashboard",
        "og_title": "aurora : Arbeon Admin Dashboard",
        "og_description": "aurora : Arbeon Admin Dashboard",
        "og_image": f"{folderName}/images/og_image.png",
        "title": "aurora : Arbeon Admin Dashboard",
    },
    "global": {
        "css": [
            f"{folderName}/vendor/bootstrap-select/dist/css/bootstrap-select.min.css",
            f"{folderName}/css/style.css",
        ],
        "js": {
            "top": [
                f"{folderName}/vendor/global/global.min.js",
                f"{folderName}/vendor/bootstrap-select/dist/js/bootstrap-select.min.js",
            ],
            "bottom": [
                f"{folderName}/js/custom.min.js",
                f"{folderName}/js/deznav-init.js",
            ],
        },
    },
    "pagelevel": {
        "aurora": {
            "aurora_views": {
                "css": {
                    "index": [
                        f"{folderName}/vendor/jqvmap/css/jqvmap.min.css",
                        f"{folderName}/vendor/chartist/css/chartist.min.css",
                        f"{folderName}/vendor/jqvmap/css/jqvmap.min.css",
                        f"{folderName}/vendor/owl-carousel/owl.carousel.css",
                    ],
                    "svc_user_status": [
                        f"{folderName}/vendor/jqvmap/css/jqvmap.min.css",
                        f"{folderName}/vendor/chartist/css/chartist.min.css",
                        f"{folderName}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "scan_status": [
                        f"{folderName}/vendor/jqvmap/css/jqvmap.min.css",
                        f"{folderName}/vendor/chartist/css/chartist.min.css",
                        f"{folderName}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "permissions": [
                        f"{folderName}/vendor/sweetalert2/dist/sweetalert2.min.css",
                    ],
                    "users": [
                        f"{folderName}/vendor/datatables/css/jquery.dataTables.min.css",
                        f"{folderName}/vendor/sweetalert2/dist/sweetalert2.min.css",
                    ],
                    "add_user": [
                        f"{folderName}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                        f"{folderName}/vendor/select2/css/select2.min.css",
                    ],
                    "edit_user": [
                        f"{folderName}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                        f"{folderName}/vendor/select2/css/select2.min.css",
                    ],
                    "role_list": [
                        f"{folderName}/vendor/sweetalert2/dist/sweetalert2.min.css",
                    ],
                    "assign_permissions_to_user": [
                        f"{folderName}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/prettify.min.css",
                        f"{folderName}/vendor/bootstrap-duallistbox/src/bootstrap-duallistbox.css",
                        f"{folderName}/vendor/bootstrap-duallistbox/dist/bootstrap-duallistbox.css",
                    ],
                    "role_add": [
                        f"{folderName}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/prettify.min.css",
                        f"{folderName}/vendor/bootstrap-duallistbox/src/bootstrap-duallistbox.css",
                        f"{folderName}/vendor/bootstrap-duallistbox/dist/bootstrap-duallistbox.css",
                    ],
                    "role_edit": [
                        f"{folderName}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/prettify.min.css",
                        f"{folderName}/vendor/bootstrap-duallistbox/src/bootstrap-duallistbox.css",
                        f"{folderName}/vendor/bootstrap-duallistbox/dist/bootstrap-duallistbox.css",
                    ],
                    "app_profile": [
                        f"{folderName}/vendor/lightgallery/css/lightgallery.min.css",
                        f"{folderName}/vendor/magnific-popup/magnific-popup.css",
                    ],
                    "svc_user_list": [
                        f"{folderName}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "object_list": [
                        f"{folderName}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "new_mgid_detail": [
                        f"{folderName}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "user_management": [
                        f"{folderName}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    # "accountid_detail": [
                    #     f"{folderName}/vendor/chartist/css/chartist.min.css"
                    # ],
                    "content_list": [
                        f"{folderName}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "report_list": [
                        f"{folderName}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "index2": [
                        f"{folderName}/vendor/jqvmap/css/jqvmap.min.css",
                        f"{folderName}/vendor/chartist/css/chartist.min.css",
                        f"{folderName}/vendor/jqvmap/css/jqvmap.min.css",
                        f"{folderName}/vendor/owl-carousel/owl.carousel.css",
                    ],
                    "my_wallet": [
                        f"{folderName}/vendor/jqvmap/css/jqvmap.min.css",
                        f"{folderName}/vendor/chartist/css/chartist.min.css",
                    ],
                    "cards_center": [
                        f"{folderName}/vendor/chartist/css/chartist.min.css",
                        f"{folderName}/vendor/owl-carousel/owl.carousel.css",
                    ],
                    "transactions": [
                        f"{folderName}/vendor/jqvmap/css/jqvmap.min.css",
                        f"{folderName}/vendor/chartist/css/chartist.min.css",
                        f"{folderName}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "transactions_details": [
                        f"{folderName}/vendor/jqvmap/css/jqvmap.min.css",
                        f"{folderName}/vendor/chartist/css/chartist.min.css",
                    ],
                    "post_details": [
                        f"{folderName}/vendor/lightgallery/css/lightgallery.min.css",
                        f"{folderName}/vendor/magnific-popup/magnific-popup.css",
                    ],
                    "email_compose": [
                        f"{folderName}/vendor/dropzone/dist/dropzone.css",
                    ],
                    "email_inbox": [],
                    "email_read": [],
                    "app_calender": [
                        f"{folderName}/vendor/fullcalendar/css/main.min.css",
                    ],
                    "ecom_product_grid": [],
                    "ecom_product_list": [
                        f"{folderName}/vendor/star-rating/star-rating-svg.css",
                    ],
                    "ecom_product_detail": [
                        f"{folderName}/vendor/star-rating/star-rating-svg.css",
                        f"{folderName}/vendor/owl-carousel/owl.carousel.css",
                    ],
                    "ecom_product_order": [],
                    "ecom_checkout": [],
                    "ecom_invoice": [
                        f"{folderName}/vendor/bootstrap-select/dist/css/bootstrap-select.min.css",
                    ],
                    "ecom_customers": [],
                    "chart_float": [],
                    "chart_morris": [],
                    "chart_chartjs": [],
                    "chart_chartist": [
                        f"{folderName}/vendor/chartist/css/chartist.min.css"
                    ],
                    "chart_sparkline": [],
                    "chart_peity": [],
                    "uc_select2": [
                        f"{folderName}/vendor/select2/css/select2.min.css",
                    ],
                    "uc_nestable": [
                        f"{folderName}/vendor/nestable2/css/jquery.nestable.min.css"
                    ],
                    "uc_noui_slider": [
                        f"{folderName}/vendor/nouislider/nouislider.min.css"
                    ],
                    "uc_sweetalert": [
                        f"{folderName}/vendor/sweetalert2/dist/sweetalert2.min.css"
                    ],
                    "uc_toastr": [f"{folderName}/vendor/toastr/css/toastr.min.css"],
                    "map_jqvmap": [f"{folderName}/vendor/jqvmap/css/jqvmap.min.css"],
                    "uc_lightgallery": [
                        f"{folderName}/vendor/lightgallery/css/lightgallery.min.css"
                    ],
                    "widget_basic": [
                        f"{folderName}/vendor/chartist/css/chartist.min.css",
                        f"{folderName}/vendor/bootstrap-select/dist/css/bootstrap-select.min.css",
                    ],
                    "form_element": [],
                    "form_wizard": [
                        f"{folderName}/vendor/jquery-smartwizard/dist/css/smart_wizard.min.css"
                    ],
                    "form_ckeditor": [],
                    "form_pickers": [
                        f"{folderName}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                        f"{folderName}/vendor/clockpicker/css/bootstrap-clockpicker.min.css",
                        f"{folderName}/vendor/jquery-asColorPicker/css/asColorPicker.min.css",
                        f"{folderName}/vendor/bootstrap-material-datetimepicker/css/bootstrap-material-datetimepicker.css",
                        f"{folderName}/vendor/pickadate/themes/default.css",
                        f"{folderName}/vendor/pickadate/themes/default.date.css",
                    ],
                    "form_validation": [],
                    "table_bootstrap_basic": [],
                    "table_datatable_basic": [
                        f"{folderName}/vendor/datatables/css/jquery.dataTables.min.css",
                    ],
                    "page_login": [],
                    "page_register": [],
                    "page_forgot_password": [],
                    "page_lock_screen": [],
                    "page_error_400": [],
                    "page_error_403": [],
                    "page_error_404": [],
                    "page_error_500": [],
                    "page_error_503": [],
                },
                "js": {
                    "index": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/owl-carousel/owl.carousel.js",
                        f"{folderName}/vendor/peity/jquery.peity.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/js/dashboard/dashboard-1.js",
                    ],
                    "permissions": [
                        f"{folderName}/vendor/sweetalert2/dist/sweetalert2.min.js",
                    ],
                    "users": [
                        f"{folderName}/vendor/sweetalert2/dist/sweetalert2.min.js",
                        f"{folderName}/vendor/datatables/js/jquery.dataTables.min.js",
                        f"{folderName}/js/plugins-init/datatables.init.js",
                    ],
                    "add_user": [
                        f"{folderName}/vendor/moment/moment.min.js",
                        f"{folderName}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                        f"{folderName}/vendor/select2/js/select2.full.min.js",
                        f"{folderName}/js/plugins-init/select2-init.js",
                    ],
                    "edit_user": [
                        f"{folderName}/vendor/moment/moment.min.js",
                        f"{folderName}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                        f"{folderName}/vendor/select2/js/select2.full.min.js",
                        f"{folderName}/js/plugins-init/select2-init.js",
                    ],
                    "role_list": [
                        f"{folderName}/vendor/sweetalert2/dist/sweetalert2.min.js",
                    ],
                    "assign_permissions_to_user": [
                        f"{folderName}/vendor/bootstrap-duallistbox/ajax/libs/popper.js/1.12.9/umd/popper.min.js",
                        f"{folderName}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/run_prettify.js",
                        f"{folderName}/vendor/bootstrap-duallistbox/dist/jquery.bootstrap-duallistbox.js",
                    ],
                    "role_add": [
                        f"{folderName}/vendor/bootstrap-duallistbox/ajax/libs/popper.js/1.12.9/umd/popper.min.js",
                        f"{folderName}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/run_prettify.js",
                        f"{folderName}/vendor/bootstrap-duallistbox/dist/jquery.bootstrap-duallistbox.js",
                    ],
                    "role_edit": [
                        f"{folderName}/vendor/bootstrap-duallistbox/ajax/libs/popper.js/1.12.9/umd/popper.min.js",
                        f"{folderName}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/run_prettify.js",
                        f"{folderName}/vendor/bootstrap-duallistbox/dist/jquery.bootstrap-duallistbox.js",
                    ],
                    "svc_user_list": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/vendor/datatables/js/jquery.dataTables.min.js",
                        f"{folderName}/js/plugins-init/datatables.init.js",
                    ],
                    "object_list": [
                        f"{folderName}/vendor/datatables/js/jquery.dataTables.min.js",
                        f"{folderName}/js/plugins-init/datatables.init.js",
                        f"{folderName}/vendor/svganimation/vivus.min.js",
                        f"{folderName}/vendor/svganimation/svg.animation.js",
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/js/plugins-init/chartjs-init.js",
                    ],
                    "new_mgid_detail": [
                        f"{folderName}/vendor/datatables/js/jquery.dataTables.min.js",
                        f"{folderName}/js/plugins-init/datatables.init.js",
                        f"{folderName}/vendor/svganimation/vivus.min.js",
                        f"{folderName}/vendor/svganimation/svg.animation.js",
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/js/plugins-init/chartjs-init.js",
                    ],
                    "user_management": [
                        f"{folderName}/vendor/datatables/js/jquery.dataTables.min.js",
                        f"{folderName}/js/plugins-init/datatables.init.js",
                        f"{folderName}/vendor/svganimation/vivus.min.js",
                        f"{folderName}/vendor/svganimation/svg.animation.js",
                    ],
                    # "accountid_detail": [
                    #     f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                    #     f"{folderName}/vendor/apexchart/apexchart.js",
                    #     f"{folderName}/vendor/chartist/js/chartist.min.js",
                    #     f"{folderName}/vendor/chartist-plugin-tooltips/js/chartist-plugin-tooltip.min.js",
                    #     f"{folderName}/js/plugins-init/chartist-init.js",
                    # ],
                    "content_list": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/vendor/datatables/js/jquery.dataTables.min.js",
                        f"{folderName}/js/plugins-init/datatables.init.js",
                    ],
                    "report_list": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/vendor/datatables/js/jquery.dataTables.min.js",
                        f"{folderName}/js/plugins-init/datatables.init.js",
                    ],
                    "index2": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/owl-carousel/owl.carousel.js",
                        f"{folderName}/vendor/peity/jquery.peity.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/js/dashboard/dashboard-1.js",
                    ],
                    "my_wallet": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/peity/jquery.peity.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/js/dashboard/my-wallet.js",
                    ],
                    "invoices": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/datatables/js/jquery.dataTables.min.js",
                    ],
                    "cards_center": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/owl-carousel/owl.carousel.js",
                        f"{folderName}/vendor/peity/jquery.peity.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/js/dashboard/cards-center.js",
                    ],
                    "transactions": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/datatables/js/jquery.dataTables.min.js",
                    ],
                    "transactions_details": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/peity/jquery.peity.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/js/dashboard/transactions-details.js",
                    ],
                    "app_profile": [
                        f"{folderName}/vendor/lightgallery/js/lightgallery-all.min.js",
                        f"{folderName}/vendor/magnific-popup/magnific-popup.js",
                    ],
                    "post_details": [
                        f"{folderName}/vendor/lightgallery/js/lightgallery-all.min.js",
                        f"{folderName}/vendor/magnific-popup/magnific-popup.js",
                    ],
                    "email_compose": [
                        f"{folderName}/vendor/dropzone/dist/dropzone.js",
                    ],
                    "email_inbox": [],
                    "email_read": [],
                    "app_calender": [
                        f"{folderName}/vendor/moment/moment.min.js",
                        f"{folderName}/vendor/fullcalendar/js/main.min.js",
                        f"{folderName}/js/plugins-init/fullcalendar-init.js",
                    ],
                    "ecom_product_grid": [],
                    "ecom_product_list": [
                        f"{folderName}/vendor/star-rating/jquery.star-rating-svg.js",
                    ],
                    "ecom_product_detail": [
                        f"{folderName}/vendor/owl-carousel/owl.carousel.js",
                        f"{folderName}/vendor/star-rating/jquery.star-rating-svg.js",
                    ],
                    "ecom_product_order": [],
                    "ecom_checkout": [
                        f"{folderName}/vendor/highlightjs/highlight.pack.min.js"
                    ],
                    "ecom_invoice": [],
                    "ecom_customers": [],
                    "chart_flot": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/vendor/flot/jquery.flot.js",
                        f"{folderName}/vendor/flot/jquery.flot.pie.js",
                        f"{folderName}/vendor/flot/jquery.flot.resize.js",
                        f"{folderName}/vendor/flot-spline/jquery.flot.spline.min.js",
                        f"{folderName}/js/plugins-init/flot-init.js",
                    ],
                    "chart_morris": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/vendor/raphael/raphael.min.js",
                        f"{folderName}/vendor/morris/morris.min.js",
                        f"{folderName}/js/plugins-init/morris-init.js",
                    ],
                    "chart_chartjs": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/js/plugins-init/chartjs-init.js",
                    ],
                    "chart_chartist": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/vendor/chartist/js/chartist.min.js",
                        f"{folderName}/vendor/chartist-plugin-tooltips/js/chartist-plugin-tooltip.min.js",
                        f"{folderName}/js/plugins-init/chartist-init.js",
                    ],
                    "chart_sparkline": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/vendor/jquery-sparkline/jquery.sparkline.min.js",
                        f"{folderName}/js/plugins-init/sparkline-init.js",
                        f"{folderName}/vendor/svganimation/vivus.min.js",
                        f"{folderName}/vendor/svganimation/svg.animation.js",
                    ],
                    "chart_peity": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/peity/jquery.peity.min.js",
                        f"{folderName}/js/plugins-init/piety-init.js",
                    ],
                    "uc_select2": [
                        f"{folderName}/vendor/select2/js/select2.full.min.js",
                        f"{folderName}/js/plugins-init/select2-init.js",
                    ],
                    "uc_nestable": [
                        f"{folderName}/vendor/nestable2/js/jquery.nestable.min.js",
                        f"{folderName}/js/plugins-init/nestable-init.js",
                    ],
                    "uc_noui_slider": [
                        f"{folderName}/vendor/nouislider/nouislider.min.js",
                        f"{folderName}/vendor/wnumb/wNumb.js",
                        f"{folderName}/js/plugins-init/nouislider-init.js",
                    ],
                    "uc_sweetalert": [
                        f"{folderName}/vendor/sweetalert2/dist/sweetalert2.min.js",
                        f"{folderName}/js/plugins-init/sweetalert.init.js",
                    ],
                    "uc_toastr": [
                        f"{folderName}/vendor/toastr/js/toastr.min.js",
                        f"{folderName}/js/plugins-init/toastr-init.js",
                    ],
                    "map_jqvmap": [
                        f"{folderName}/vendor/jqvmap/js/jquery.vmap.min.js",
                        f"{folderName}/vendor/jqvmap/js/jquery.vmap.world.js",
                        f"{folderName}/vendor/jqvmap/js/jquery.vmap.usa.js",
                        f"{folderName}/js/plugins-init/jqvmap-init.js",
                    ],
                    "uc_lightgallery": [
                        f"{folderName}/vendor/lightgallery/js/lightgallery-all.min.js"
                    ],
                    "widget_basic": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/vendor/chartist/js/chartist.min.js",
                        f"{folderName}/vendor/chartist-plugin-tooltips/js/chartist-plugin-tooltip.min.js",
                        f"{folderName}/vendor/flot/jquery.flot.js",
                        f"{folderName}/vendor/flot/jquery.flot.pie.js",
                        f"{folderName}/vendor/flot/jquery.flot.resize.js",
                        f"{folderName}/vendor/flot-spline/jquery.flot.spline.min.js",
                        f"{folderName}/vendor/jquery-sparkline/jquery.sparkline.min.js",
                        f"{folderName}/js/plugins-init/sparkline-init.js",
                        f"{folderName}/vendor/peity/jquery.peity.min.js",
                        f"{folderName}/js/plugins-init/piety-init.js",
                        f"{folderName}/js/plugins-init/widgets-script-init.js",
                    ],
                    "form_element": [],
                    "form_wizard": [
                        f"{folderName}/vendor/jquery-steps/build/jquery.steps.min.js",
                        f"{folderName}/vendor/jquery-validation/jquery.validate.min.js",
                        f"{folderName}/js/plugins-init/jquery.validate-init.js",
                        f"{folderName}/vendor/jquery-smartwizard/dist/js/jquery.smartWizard.js",
                    ],
                    "form_ckeditor": [f"{folderName}/vendor/ckeditor/ckeditor.js"],
                    "form_pickers": [
                        f"{folderName}/vendor/bootstrap-select/dist/js/bootstrap-select.min.js",
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/vendor/moment/moment.min.js",
                        f"{folderName}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                        f"{folderName}/vendor/clockpicker/js/bootstrap-clockpicker.min.js",
                        f"{folderName}/vendor/jquery-asColor/jquery-asColor.min.js",
                        f"{folderName}/vendor/jquery-asGradient/jquery-asGradient.min.js",
                        f"{folderName}/vendor/jquery-asColorPicker/js/jquery-asColorPicker.min.js",
                        f"{folderName}/vendor/bootstrap-material-datetimepicker/js/bootstrap-material-datetimepicker.js",
                        f"{folderName}/vendor/pickadate/picker.js",
                        f"{folderName}/vendor/pickadate/picker.time.js",
                        f"{folderName}/vendor/pickadate/picker.date.js",
                        f"{folderName}/js/plugins-init/bs-daterange-picker-init.js",
                        f"{folderName}/js/plugins-init/clock-picker-init.js",
                        f"{folderName}/js/plugins-init/jquery-asColorPicker.init.js",
                        f"{folderName}/js/plugins-init/material-date-picker-init.js",
                        f"{folderName}/js/plugins-init/pickadate-init.js",
                    ],
                    "form_validation": [],
                    "table_bootstrap_basic": [],
                    "table_datatable_basic": [
                        f"{folderName}/vendor/chart.js/Chart.bundle.min.js",
                        f"{folderName}/vendor/apexchart/apexchart.js",
                        f"{folderName}/vendor/datatables/js/jquery.dataTables.min.js",
                        f"{folderName}/js/plugins-init/datatables.init.js",
                    ],
                    "page_login": [],
                    "page_register": [],
                    "page_forgot_password": [],
                    "page_lock_screen": [],
                    "page_error_400": [],
                    "page_error_403": [],
                    "page_error_404": [],
                    "page_error_500": [],
                    "page_error_503": [],
                },
            }
        }
    },
}
