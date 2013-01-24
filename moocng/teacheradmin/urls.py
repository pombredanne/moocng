# Copyright 2012 Rooter Analysis S.L.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'moocng.teacheradmin.views',

    url(r'^$', 'teacheradmin_stats', name='teacheradmin_stats'),

    url(r'^units/$', 'teacheradmin_units', name='teacheradmin_units'),
    url(r'^units/forcevideoprocess$', 'teacheradmin_units_forcevideoprocess',
        name='teacheradmin_units_forcevideoprocess'),
    url(r'^units/question/(?P<kq_id>\d+)$', 'teacheradmin_units_question',
        name='teacheradmin_units_question'),
    url(r'^units/question/(?P<kq_id>\d+)/(?P<option_id>\d+)$',
        'teacheradmin_units_option', name='teacheradmin_units_option'),

    url(r'^teachers/$', 'teacheradmin_teachers', name='teacheradmin_teachers'),
    url(r'^teachers/(?P<email_or_id>[^/]+)/$', 'teacheradmin_teachers_delete',
        name='teacheradmin_teachers_delete'),
    url(r'^teachers/invite$', 'teacheradmin_teachers_invite',
        name='teacheradmin_teachers_invite'),
    url(r'^teachers/transfer$', 'teacheradmin_teachers_transfer',
        name='teacheradmin_teachers_transfer'),

    url(r'^students/$', 'teacheradmin_students', name='teacheradmin_students'),
    url(r'^students/(?P<student_id>[^/]+)/$', 'teacheradmin_students_delete',
        name='teacheradmin_students_delete'),
    url(r'^students/enrol$', 'teacheradmin_students_enrol',
        name='teacheradmin_students_enrol'),

    url(r'^info/$', 'teacheradmin_info', name='teacheradmin_info'),

    url(r'^announcements/$', 'teacheradmin_announcements',
        name='teacheradmin_announcements'),
    url(r'^announcements/add', 'teacheradmin_announcements_edit',
        name='teacheradmin_announcements_add'),
    url(r'^announcements/(?P<announ_slug>[^/]+)/edit/$', 'teacheradmin_announcements_edit',
        name='teacheradmin_announcements_edit'),
    url(r'^announcements/(?P<announ_slug>[^/]+)/$', 'teacheradmin_announcements_view',
        name='teacheradmin_announcements_view'),
    url(r'^announcements/(?P<announ_slug>[^/]+)/delete$', 'teacheradmin_announcements_delete',
        name='teacheradmin_announcements_delete'),

    url(r'^emails/$', 'teacheradmin_emails', name='teacheradmin_emails'),
)
