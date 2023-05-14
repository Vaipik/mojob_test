## Steps how to start project

1. Python 3.10
2. Install poetry
3. Run `poetry install` in `base directory`
4. In `base directory` create `.env` file according to given example
5. Run `python src/manage.py migrate`
6. And finally run `python src/manage.py runserver`

___
To run test in your shell `python src/manage.py tests` when you are in base directory
___

### Available endpoints

<table>
<thead>
<tr>
    <th>Endpoint</th>
    <th>Method</th>
    <th>Result</th>
</tr>
</thead>
<tbody>
<tr>
    <td>/api/v1/jobs/</td>
    <td>GET</td>
    <td>List of all created/available jobs</td>
</tr>
<tr>
    <td>/api/v1/jobs/</td>
    <td>POST</td>
    <td>Publish new job</td>
</tr>
<tr>
    <td>/api/v1/jobs/{uuid}</td>
    <td>GET</td>
    <td>Detailed information about job</td>
</tr>
<tr>
    <td>/api/v1/jobs/{uuid}</td>
    <td>PUT</td>
    <td>Update job data</td>
</tr>
<tr>
    <td>/api/v1/jobs/{uuid}</td>
    <td>DELETE</td>
    <td>Delete job</td>
</tr>
<tr>
    <td>/api/v1/users/{int}/applications/</td>
    <td>GET</td>
    <td>List of all user job applications</td>
</tr>
</tbody>
</table>

___

Some picture to see how it works: \
The response from endpoint `/api/v1/jobs/` if user is authorized
<img height="320" src="/home/nkhylko/IT/TEST_TASKS/Mojob_test/docs/img/jobs_get_list_auth.png" width="640"/>
The response from endpoint `/api/v1/jobs/` if user is unauthorized
All further examples will be for authorized user
<img height="320" src="/home/nkhylko/IT/TEST_TASKS/Mojob_test/docs/img/jobs_get_unauth.png" width="640"/>
The response from endpoint `/api/v1/jobs/` for `POST` method.
<img height="320" src="/home/nkhylko/IT/TEST_TASKS/Mojob_test/docs/img/jobs_post.png" width="640"/>
The response from endpoint `/api/v1/jobs/` for `POST` method with wrong `job type`
<img height="320" src="/home/nkhylko/IT/TEST_TASKS/Mojob_test/docs/img/jobs_post_with_wrong_type.png" width="640"/>
The response from endpoint `/api/v1/jobs/{uuid}` for `PUT` method.
<img height="320" src="/home/nkhylko/IT/TEST_TASKS/Mojob_test/docs/img/jobs_put.png" width="640"/>
The response from endpoint `/api/v1/jobs/{uuid}` for `DELETE` method.
<img height="320" src="/home/nkhylko/IT/TEST_TASKS/Mojob_test/docs/img/jobs_delete.png" width="640"/>
The response from endpoint `/api/v1/users/{id}/applications/` for `GET` method.
<img height="320" src="/home/nkhylko/IT/TEST_TASKS/Mojob_test/docs/img/applications_get_list.png" width="640"/>
