from django.db import models

# Create your models here.
class Prompt(models.Model):

    '''Model to store prompts for the RAG application.
    This model includes fields for the Prompt text, the user who created it
    and the timestamp of creation.
    '''
    # user_name = models.TextField(auto_created=True)  
    prompt_text = models.TextField(blank=False, null=False, verbose_name="Prompt Text")
    
    class Meta:
        verbose_name = _("Prompt")
        verbose_name_plural = _("Prompts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Prompt_detail", kwargs={"pk": self.pk})
