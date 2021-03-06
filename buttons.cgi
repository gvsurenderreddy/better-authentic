#!/usr/bin/perl5.18

#
# Authentic Theme 12.00 (https://github.com/qooob/authentic-theme)
# Copyright 2015 Ilia Rostovtsev <programming@rostovtsev.ru>
# Licensed under MIT (https://github.com/qooob/authentic-theme/blob/master/LICENSE)
#

$user = $remote_user;
print '<li class="user-link">';
if ( &foreign_available("acl") ) {
    print '<a target="page" data-href="/acl/edit_user.cgi" href="'
        . $gconfig{'webprefix'}
        . '/acl/edit_user.cgi?user='
        . $user
        . '"><i class="fa fa-fw fa-user"></i>&nbsp;&nbsp;'
        . $user . '</a>';
}
else {
    print
        '<a style="pointer-events: none;"><i class="fa fa-fw fa-user"></i>&nbsp;&nbsp;'
        . $user . '</a>';
}
print '</li><li class="user-link __logout-link">';

&get_miniserv_config( \%miniserv );

if (   $miniserv{'logout'}
    && !$ENV{'SSL_USER'}
    && !$ENV{'LOCAL_USER'}
    && $ENV{'HTTP_USER_AGENT'} !~ /webmin/i )
{

    if ($main::session_id) {
        print '<a href="'
            . $gconfig{'webprefix'}
            . '/session_login.cgi?logout=1"><i class="fa fa-fw fa-sign-out text-danger"></i></a>';
    }
    else {
        print '<a href="'
            . $gconfig{'webprefix'}
            . '/switch_user.cgi"><i class="fa fa-fw fa-exchange text-danger"></i></a>';
    }
}

print '</li>';

if (   -r "$root_directory/virtual-server/edit_lang.cgi"
    && __settings('settings_leftmenu_button_language') eq 'true'
    && (   $is_virtualmin != -1
        || $is_cloudmin != -1
        || $in{'xhr-buttons-type'} eq '1' )
    )
{
    print '<li class="user-link">
                    <a target="page" href="/virtual-server/edit_lang.cgi">
                        <i class="fa fa-fw fa-globe"></i>
                    </a>
                </li>';
}
elsif ( &foreign_available("change-user")
    && __settings('settings_leftmenu_button_language') eq 'true' )
{
    print
        '<li class="user-link"><a target="page" href="/change-user"><i class="fa fa-fw fa-globe"></i></a></li>';
}

if ( __settings('settings_leftmenu_button_refresh') ne 'false' ) {
    print
        '<li class="user-link"><a data-refresh="true" style="cursor: pointer"><i class="fa fa-fw fa-refresh"></i></a></li>';
}
