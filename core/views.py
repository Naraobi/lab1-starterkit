# core/views.py
from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.utils import translation
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    return render(request, 'metro62/index.html')

def dashboard_projects(request):
    return render(request, 'metro62/dashboards/projects.html')

def dashboard_ecommerce(request):
    return render(request, 'metro62/dashboards/ecommerce.html')

def dashboard_bidding(request):
    return render(request, 'metro62/dashboards/bidding.html')

def dashboard_callcenter(request):
    return render(request, 'metro62/dashboards/call-center.html')

def dashboard_crypto(request):
    return render(request, 'metro62/dashboards/crypto.html')

def dashboard_delivery(request):
    return render(request, 'metro62/dashboards/delivery.html')

def dashboard_financeperformance(request):
    return render(request, 'metro62/dashboards/finance-performance.html')

def dashboard_logistics(request):
    return render(request, 'metro62/dashboards/logistics.html')

def dashboard_marketing(request):
    return render(request, 'metro62/dashboards/marketing.html')

def dashboard_onlinecourses(request):
    return render(request, 'metro62/dashboards/online-courses.html')

def dashboard_podcast(request):
    return render(request, 'metro62/dashboards/podcast.html')

def dashboard_pos(request):
    return render(request, 'metro62/dashboards/pos.html')

def dashboard_school(request):
    return render(request, 'metro62/dashboards/school.html')

def dashboard_social(request):
    return render(request, 'metro62/dashboards/social.html')

def dashboard_storeanalytics(request):
    return render(request, 'metro62/dashboards/store-analytics.html')

def dashboard_websiteanalytics(request):
    return render(request, 'metro62/dashboards/website-analytics.html')

def pages_about(request):
    return render(request, 'metro62/pages/about.html')

def pages_contact(request):
    return render(request, 'metro62/pages/contact.html')

def pages_faq(request):
    return render(request, 'metro62/pages/faq.html')

def pages_licenses(request):
    return render(request, 'metro62/pages/licenses.html')

def pages_pricing(request):
    return render(request, 'metro62/pages/pricing.html')

def pages_sitemap(request):
    return render(request, 'metro62/pages/sitemap.html')

def pages_team(request):
    return render(request, 'metro62/pages/team.html')

def pages_activity(request):
    return render(request, 'metro62/pages/user-profile/activity.html')

def pages_userprofile_campaigns(request):
    return render(request, 'metro62/pages/user-profile/campaigns.html')

def pages_userprofile_documents(request):
    return render(request, 'metro62/pages/user-profile/documents.html')

def pages_userprofile_followers(request):
    return render(request, 'metro62/pages/user-profile/followers.html')

def pages_userprofile_overview(request):
    return render(request, 'metro62/pages/user-profile/overview.html')

def pages_userprofile_projects(request):
    return render(request, 'metro62/pages/user-profile/projects.html')

def account_activity(request):
    return render(request, 'metro62/account/activity.html')

def account_apikeys(request):
    return render(request, 'metro62/account/api-keys.html')

def account_billing(request):
    return render(request, 'metro62/account/billing.html')

def account_logs(request):
    return render(request, 'metro62/account/logs.html')

def account_overview(request):
    return render(request, 'metro62/account/overview.html')

def account_referrals(request):
    return render(request, 'metro62/account/referrals.html')

def account_security(request):
    return render(request, 'metro62/account/security.html')

def account_settings(request):
    return render(request, 'metro62/account/settings.html')

def account_statements(request):
    return render(request, 'metro62/account/statements.html')

def appchat_drawer(request):
    return render(request, 'metro62/apps/chat/drawer.html')

def appchat_group(request):
    return render(request, 'metro62/apps/chat/group.html')

def appchat_private(request):
    return render(request, 'metro62/apps/chat/private.html')

def appcontacts_addcontact(request):
    return render(request, 'metro62/apps/contacts/add-contact.html')

def appcontacts_editcontact(request):
    return render(request, 'metro62/apps/contacts/edit-contact.html')

def appcontacts_gettingstarted(request):
    return render(request, 'metro62/apps/contacts/getting-started.html')

def appcontacts_viewcontact(request):
    return render(request, 'metro62/apps/contacts/view-contact.html')

def appcustomers_gettingstarted(request):
    return render(request, 'metro62/apps/customers/getting-started.html')

def appcustomers_list(request):
    return render(request, 'metro62/apps/customers/list.html')

def appcustomers_view(request):
    return render(request, 'metro62/apps/customers/view.html')

def appecommerce_catalog_addcategory(request):
    return render(request, 'metro62/apps/ecommerce/catalog/add-category.html')

def appecommerce_catalog_addproduct(request):
    return render(request, 'metro62/apps/ecommerce/catalog/add-product.html')

def appecommerce_catalog_categories(request):
    return render(request, 'metro62/apps/ecommerce/catalog/categories.html')

def appecommerce_catalog_editcategory(request):
    return render(request, 'metro62/apps/ecommerce/catalog/edit-category.html')

def appecommerce_catalog_editproduct(request):
    return render(request, 'metro62/apps/ecommerce/catalog/edit-product.html')

def appecommerce_catalog_products(request):
    return render(request, 'metro62/apps/ecommerce/catalog/products.html')

def appecommerce_customers_details(request):
    return render(request, 'metro62/apps/ecommerce/customers/details.html')

def appecommerce_customers_listing(request):
    return render(request, 'metro62/apps/ecommerce/customers/listing.html')

def appecommerce_reports_customerorders(request):
    return render(request, 'metro62/apps/ecommerce/reports/customer-orders.html')

def appecommerce_reports_returns(request):
    return render(request, 'metro62/apps/ecommerce/reports/returns.html')

def appecommerce_reports_sales(request):
    return render(request, 'metro62/apps/ecommerce/reports/sales.html')

def appecommerce_reports_shipping(request):
    return render(request, 'metro62/apps/ecommerce/reports/shipping.html')

def appecommerce_reports_view(request):
    return render(request, 'metro62/apps/ecommerce/reports/view.html')

def appecommerce_sales_addorder(request):
    return render(request, 'metro62/apps/ecommerce/sales/add-order.html')

def appecommerce_sales_details(request):
    return render(request, 'metro62/apps/ecommerce/sales/details.html')

def appecommerce_sales_editorder(request):
    return render(request, 'metro62/apps/ecommerce/sales/edit-order.html')

def appecommerce_sales_listing(request):
    return render(request, 'metro62/apps/ecommerce/sales/listing.html')

def appecommerce_settings(request):
    return render(request, 'metro62/apps/ecommerce/settings.html')

def appfilemanager_blank(request):
    return render(request, 'metro62/apps/file-manager/blank.html')

def appfilemanager_files(request):
    return render(request, 'metro62/apps/file-manager/files.html')

def appfilemanager_folders(request):
    return render(request, 'metro62/apps/file-manager/folders.html')

def appfilemanager_settings(request):
    return render(request, 'metro62/apps/file-manager/settings.html')

def appinbox_compose(request):
    return render(request, 'metro62/apps/inbox/compose.html')

def appinbox_listing(request):
    return render(request, 'metro62/apps/inbox/listing.html')

def appinbox_reply(request):
    return render(request, 'metro62/apps/inbox/reply.html')

def appinvoices_create(request):
    return render(request, 'metro62/apps/invoices/create.html')

def appinvoices_view_invoice1(request):
    return render(request, 'metro62/apps/invoices/view/invoice-1.html')

def appinvoices_view_invoice2(request):
    return render(request, 'metro62/apps/invoices/view/invoice-2.html')

def appinvoices_view_invoice3(request):
    return render(request, 'metro62/apps/invoices/view/invoice-3.html')

def appprojects_activity(request):
    return render(request, 'metro62/apps/projects/activity.html')

def appprojects_budget(request):
    return render(request, 'metro62/apps/projects/budget.html')

def appprojects_files(request):
    return render(request, 'metro62/apps/projects/files.html')

def appprojects_list(request):
    return render(request, 'metro62/apps/projects/list.html')

def appprojects_project(request):
    return render(request, 'metro62/apps/projects/project.html')

def appprojects_settings(request):
    return render(request, 'metro62/apps/projects/settings.html')

def appprojects_targets(request):
    return render(request, 'metro62/apps/projects/targets.html')

def appprojects_users(request):
    return render(request, 'metro62/apps/projects/users.html')

def appsubscriptions_add(request):
    return render(request, 'metro62/apps/subscriptions/add.html')

def appsubscriptions_gettingstarted(request):
    return render(request, 'metro62/apps/subscriptions/getting-started.html')

def appsubscriptions_list(request):
    return render(request, 'metro62/apps/subscriptions/list.html')

def appsubscriptions_view(request):
    return render(request, 'metro62/apps/subscriptions/view.html')

def appsupportcenter_contact(request):
    return render(request, 'metro62/apps/support-center/contact.html')

def appsupportcenter_faq(request):
    return render(request, 'metro62/apps/support-center/faq.html')

def appsupportcenter_licenses(request):
    return render(request, 'metro62/apps/support-center/licenses.html')

def appsupportcenter_overview(request):
    return render(request, 'metro62/apps/support-center/overview.html')

def appsupportcenter_tickets_list(request):
    return render(request, 'metro62/apps/support-center/tickets/list.html')

def appsupportcenter_tickets_view(request):
    return render(request, 'metro62/apps/support-center/tickets/view.html')

def appsupportcenter_tutorials_list(request):
    return render(request, 'metro62/apps/support-center/tutorials/list.html')

def appsupportcenter_tutorials_post(request):
    return render(request, 'metro62/apps/support-center/tutorials/post.html')

def appusermanagement_permissions(request):
    return render(request, 'metro62/apps/user-management/permissions.html')

def appusermanagement_roles_list(request):
    return render(request, 'metro62/apps/user-management/roles/list.html')

def appusermanagement_roles_view(request):
    return render(request, 'metro62/apps/user-management/roles/view.html')

def appusermanagement_users_list(request):
    return render(request, 'metro62/apps/user-management/users/list.html')

def appusermanagement_users_view(request):
    return render(request, 'metro62/apps/user-management/users/view.html')

def app_calendar(request):
    return render(request, 'metro62/apps/calendar.html')

def authentication_email_carddeclined(request):
    return render(request, 'metro62/authentication/email/card-declined.html')

def authentication_email_invitation(request):
    return render(request, 'metro62/authentication/email/invitation.html')

def authentication_email_passwordchange(request):
    return render(request, 'metro62/authentication/email/password-change.html')

def authentication_email_passwordreset(request):
    return render(request, 'metro62/authentication/email/password-reset.html')

def authentication_email_promo1(request):
    return render(request, 'metro62/authentication/email/promo-1.html')

def authentication_email_promo2(request):
    return render(request, 'metro62/authentication/email/promo-2.html')

def authentication_email_promo3(request):
    return render(request, 'metro62/authentication/email/promo-3.html')

def authentication_email_resetpassword(request):
    return render(request, 'metro62/authentication/email/reset-password.html')

def authentication_email_subscriptionconfirmed(request):
    return render(request, 'metro62/authentication/email/subscription-confirmed.html')

def authentication_email_verifyemail(request):
    return render(request, 'metro62/authentication/email/verify-email.html')

def authentication_email_welcomemessage(request):
    return render(request, 'metro62/authentication/email/welcome-message.html')

def authentication_extended_multistepssignup(request):
    return render(request, 'metro62/authentication/extended/multi-steps-sign-up.html')

def authentication_extended_twofactorauth(request):
    return render(request, 'metro62/authentication/extended/two-factor-auth.html')

def authentication_general_accountdeactivated(request):
    return render(request, 'metro62/authentication/general/account-deactivated.html')

def authentication_general_comingsoon(request):
    return render(request, 'metro62/authentication/general/coming-soon.html')

def authentication_general_deactivation(request):
    return render(request, 'metro62/authentication/general/deactivation.html')

def authentication_general_error404(request):
    return render(request, 'metro62/authentication/general/error-404.html')

def authentication_general_error500(request):
    return render(request, 'metro62/authentication/general/error-500.html')

def authentication_general_passwordconfirmation(request):
    return render(request, 'metro62/authentication/general/password-confirmation.html')

def authentication_general_verifyemail(request):
    return render(request, 'metro62/authentication/general/verify-email.html')

def authentication_general_welcome(request):
    return render(request, 'metro62/authentication/general/welcome.html')

def authentication_layouts_corporate_newpassword(request):
    return render(request, 'metro62/authentication/layouts/corporate/new-password.html')

def authentication_corporate_resetpassword(request):
    return render(request, 'metro62/authentication/layouts/corporate/reset-password.html')

def authentication_layouts_corporate_signin(request):
    return render(request, 'metro62/authentication/layouts/corporate/sign-in.html')

def authentication_layouts_corporate_signup(request):
    return render(request, 'metro62/authentication/layouts/corporate/sign-up.html')

def authentication_layouts_corporate_twofactor(request):
    return render(request, 'metro62/authentication/layouts/corporate/two-factor.html')

def authentication_layouts_creative_newpassword(request):
    return render(request, 'registration/new-password.html')

def authentication_layouts_creative_resetpassword(request):
    return render(request, 'registration/reset-password.html')

# --------------------------
# SIGNUP / REGISTRATION VIEW
# --------------------------


def authentication_layouts_creative_signin(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)

                # Activate user's default language
                profile = user.profiles.first()  # assuming one profile for demo
                translation.activate(profile.default_language)
                request.session[translation.LANGUAGE_SESSION_KEY] = profile.default_language

                return redirect('home')
            else:
                error = "Invalid credentials"
        except User.DoesNotExist:
            error = "User with that email does not exist"
        return render(request, 'registration/login.html', {'error': error})

    return render(request, 'registration/login.html')


def authentication_layouts_creative_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            return render(request, 'registration/sign-up.html', {'error': 'Please fill required fields'})

        if User.objects.filter(email=email).exists():
            return render(request, 'registration/sign-up.html', {'error': 'Email already registered'})

        # Create user; username is optional or auto-generated if you require it
        user = User.objects.create_user(email=email, password=password)
        user.save()
        return redirect('login')    # Django login URL name

    return render(request, 'registration/sign-up.html')


def logout_view(request):
    logout(request)
    return redirect('authentication-layouts-creative-signin')

def authentication_layouts_creative_twofactor(request):
    return render(request, 'metro62/authentication/layouts/creative/twofactor.html')

def authentication_layouts_fancy_newpassword(request):
    return render(request, 'metro62/authentication/layouts/fancy/new-password.html')

def authentication_layouts_fancy_resetpassword(request):
    return render(request, 'metro62/authentication/layouts/fancy/reset-password.html')

def authentication_layouts_fancy_signin(request):
    return render(request, 'metro62/authentication/layouts/fancy/sign-in.html')

def authentication_layouts_fancy_signup(request):
    return render(request, 'metro62/authentication/layouts/fancy/sign-up.html')

def authentication_layouts_fancy_twofactor(request):
    return render(request, 'metro62/authentication/layouts/fancy/twofactor.html')

def authentication_layouts_overlay_newpassword(request):
    return render(request, 'metro62/authentication/layouts/overlay/new-password.html')

def authentication_layouts_overlay_resetpassword(request):
    return render(request, 'metro62/authentication/layouts/overlay/reset-password.html')

def authentication_layouts_overlay_signin(request):
    return render(request, 'metro62/authentication/layouts/overlay/sign-in.html')

def authentication_layouts_overlay_signup(request):
    return render(request, 'metro62/authentication/layouts/overlay/sign-up.html')

def authentication_layouts_overlay_twofactor(request):
    return render(request, 'metro62/authentication/layouts/overlay/twofactor.html')

def pages_social_activity(request):
    return render(request, 'metro62/pages/social/activity.html')

def pages_social_feeds(request):
    return render(request, 'metro62/pages/social/feeds.html')

def pages_social_followers(request):
    return render(request, 'metro62/pages/social/followers.html')

def pages_social_settings(request):
    return render(request, 'metro62/pages/social/settings.html')

def pages_pricing_table(request):
    return render(request, 'metro62/pages/pricing/table.html')

def pages_faq_classic(request):
    return render(request, 'metro62/pages/faq/classic.html')

def pages_faq_extended(request):
    return render(request, 'metro62/pages/faq/extended.html')

def pages_careers_apply(request):
    return render(request, 'metro62/pages/careers/apply.html')

def pages_careers_list(request):
    return render(request, 'metro62/pages/careers/list.html')

def pages_blog_home(request):
    return render(request, 'metro62/pages/blog/home.html')

def pages_blog_post(request):
    return render(request, 'metro62/pages/blog/post.html')

def utilities_modals_forms_bidding(request):
    return render(request, 'metro62/utilities/modals/forms/bidding.html')

def utilities_modals_forms_creatapikeys(request):
    return render(request, 'metro62/utilities/modals/forms/create-api-key.html')

def utilities_modals_forms_newaddress(request):
    return render(request, 'metro62/utilities/modals/forms/new-address.html')

def utilities_modals_forms_newcard(request):
    return render(request, 'metro62/utilities/modals/forms/new-card.html')

def utilities_modals_forms_newtarget(request):
    return render(request, 'metro62/utilities/modals/forms/new-target.html')

def utilities_modals_general_invitefriends(request):
    return render(request, 'metro62/utilities/modals/general/invite-friends.html')

def utilities_modals_general_selectusers(request):
    return render(request, 'metro62/utilities/modals/general/select-users.html')

def utilities_modals_general_shareearn(request):
    return render(request, 'metro62/utilities/modals/general/share-earn.html')

def utilities_modals_general_upgradeplan(request):
    return render(request, 'metro62/utilities/modals/general/upgrade-plan.html')

def utilities_modals_general_viewusers(request):
    return render(request, 'metro62/utilities/modals/general/view-users.html')

def utilities_modals_search_selectlocation(request):
    return render(request, 'metro62/utilities/modals/search/select-location.html')

def utilities_modals_search_users(request):
    return render(request, 'metro62/utilities/modals/search/users.html')

def utilities_modals_wizards_createapp(request):
    return render(request, 'metro62/utilities/modals/wizards/create-app.html')

def utilities_modals_wizards_createaccount(request):
    return render(request, 'metro62/utilities/modals/wizards/create-account.html')

def utilities_modals_wizards_createcampaign(request):
    return render(request, 'metro62/utilities/modals/wizards/create-campaign.html')

def utilities_modals_wizards_createproject(request):
    return render(request, 'metro62/utilities/modals/wizards/create-project.html')

def utilities_modals_wizards_offeradeal(request):
    return render(request, 'metro62/utilities/modals/wizards/offer-a-deal.html')

def utilities_modals_wizards_topupwallet(request):
    return render(request, 'metro62/utilities/modals/wizards/top-up-wallet.html')

def utilities_modals_wizards_twofactorauthentication(request):
    return render(request, 'metro62/utilities/modals/wizards/two-factor-authentication.html')

def utilities_search_horizontal(request):
    return render(request, 'metro62/utilities/search/horizontal.html')

def utilities_search_selectlocation(request):
    return render(request, 'metro62/utilities/search/select-location.html')

def utilities_search_users(request):
    return render(request, 'metro62/utilities/search/users.html')

def utilities_search_vertical(request):
    return render(request, 'metro62/utilities/search/vertical.html')

def utilities_wizards_createapp(request):
    return render(request, 'metro62/utilities/wizards/create-app.html')

def utilities_wizards_createaccount(request):
    return render(request, 'metro62/utilities/wizards/create-account.html')

def utilities_wizards_createcampaign(request):
    return render(request, 'metro62/utilities/wizards/create-campaign.html')

def utilities_wizards_createproject(request):
    return render(request, 'metro62/utilities/wizards/create-project.html')

def utilities_wizards_offeradeal(request):
    return render(request, 'metro62/utilities/wizards/offer-a-deal.html')

def utilities_wizards_horizontal(request):
    return render(request, 'metro62/utilities/wizards/horizontal.html')

def utilities_wizards_twofactorauthentication(request):
    return render(request, 'metro62/utilities/wizards/two-factor-authentication.html')

def utilities_wizards_vertical(request):
    return render(request, 'metro62/utilities/wizards/vertical.html')

def widgets_charts(request):
    return render(request, 'metro62/widgets/charts.html')

def widgets_feeds(request):
    return render(request, 'metro62/widgets/feeds.html')

def widgets_lists(request):
    return render(request, 'metro62/widgets/lists.html')

def widgets_mixed(request):
    return render(request, 'metro62/widgets/mixed.html')

def widgets_statistics(request):
    return render(request, 'metro62/widgets/statistics.html')

def widgets_tables(request):
    return render(request, 'metro62/widgets/tables.html')

def landing(request):
    return render(request, 'metro62/landing.html')