"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from xblock.core import XBlock
# from xblock.fields import Integer, String, Scope, Dict, Float, Boolean
from xblock.fields import Integer, Scope, String
# from xblock.fragment import Fragment
# McDaniel apr-2019: this is deprecated.
from web_fragments.fragment import Fragment
# from xblock.scorable import ScorableXBlockMixin, Score
from xblockutils.studio_editable import StudioEditableXBlockMixin
from logging import getLogger
logger = getLogger(__name__)


class GeoGebraXBlock(XBlock):

    """
    TO-DO: document what your XBlock does.
    """

    has_author_view = True # tells the xblock to not ignore the AuthorView

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    display_name = String(help="block name", default="GeoGebra", scope=Scope.content)

    ggb_url = String(help="GGB filename or URL e.g https://cdn.querium.com/geogebra/XXXXX.ggb", default="", scope=Scope.content)

    # Hidden field to save the UUID for this instance of the Xblock.
    url_name = String(help="UUID of this instance", default="NONE", scope=Scope.content)


    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the GeoGebraXBlock, shown to students
        when viewing courses.
        """

	    # mcdaniel jul-2020: fix indentation error
        logger.info("geogebra student_view ggb_url={a}".format(a=self.ggb_url))


        """
        Ensure that the ggb_url attribute is defined in this xblock
        """

        ggburl = ""

        try:
            ggburl = self.ggb_url
        except NameError:
            ggburl = ""

        data = {
                "ggb_url" : ggburl
                }

        html = self.resource_string("static/html/geogebra.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/geogebra.css"))
        frag.add_javascript_url("https://cdn.geogebra.org/apps/deployggb.js")
        frag.add_javascript(self.resource_string("static/js/src/geogebra.js"))
        frag.initialize_js('GeoGebraXBlock',data)
        return frag

    # SAVE GGB URL
    @XBlock.json_handler
    def save_question(self, data, suffix=''):
        logger.info('save_question() - entered')
        self.ggb_url = data['ggb_url']

        self.display_name = "GeoGebra"

        print self.display_name
        return {'result': 'success'}

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("GeoGebraXBlock",
             """<geogebra/>
             """),
            ("Multiple GeoGebraXBlock",
             """<vertical_demo>
                <geogebra/>
                <geogebra/>
                <geogebra/>
                </vertical_demo>
             """),
        ]

    def studio_view(self, context=None):
        logger.info('geogebra xblock studio_view() - entered')
        """
        The STUDIO view of the GeoGebraXblock, shown to instructors
        when authoring courses.
        """
        html = self.resource_string("static/html/geogebraxstudio.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/geogebraxstudio.css"))
        frag.add_javascript(self.resource_string("static/js/src/geogebraxstudio.js"))

        frag.initialize_js('GeoGebraxStudio')
        return frag

    def author_view(self, context=None):
        logger.info('geogebra xblock author_view() - entered')
        """
        The AUTHOR view of the GeoGebraXblock, shown to instructors
        when previewing courses.
        """
        html = self.resource_string("static/html/geogebraxauthor.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/geogebraxauthor.css"))
        frag.add_javascript(self.resource_string("static/js/src/geogebraxauthor.js"))

        frag.initialize_js('GeoGebraxAuthor')
        return frag
