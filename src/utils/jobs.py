class JobEmail:

    def send_job_created_mail(self, job_id):
        print("JOB CREATED")

    def send_job_updated_mail(self, job_id, old_title_rich_text, new_title_rich_text):
        print("JOB UPDATED")
        print("OLD JOD TITLE: {}".format(old_title_rich_text))
        print("NEW JOB TITLE: {}".format(new_title_rich_text))
