from random import randint

from crispy_forms.layout import Layout, HTML, Field, Fieldset, ButtonHolder, Submit, Div


def get_edit_post_layout(instance=None):
    """
    this is so terrible that i'm doing this. 1/99999 chance to fail, but w/e.
    """
    if instance:
        instance_id = instance.id
    else:
        instance_id = None

    return Layout(
        Fieldset(
            '',
            Field('place_id', id="id_edit_place_id"),
            Div(
                Div('title', css_class="col s12 m4"),
                Div('headline', css_class="col s12 m8"),
                css_class="row"
            ),
            Div(
                HTML('<input id="post-edit-map-input" class="controls" type="text" placeholder="Enter a location"><div id="post-edit-map" class="blog-form-map"></div>'),
                Div(Field('public', id="id_edit_public"), css_class="col m6 s12"),
                css_class="row"
            ),
            Div(
                Div('image', css_class="col m6 s12"),
                Div('image_description', css_class="col m6 s12"),
                css_class="row"
            ),
            Div(
                Div(Field('body', id="id_edit_body_%s" % randint(0,99999)), css_class="col s12"),
                css_class="row"
            )
        ),
        ButtonHolder(
            Submit('submit', 'Save', css_class='btn right hover-right')
        )
    )
