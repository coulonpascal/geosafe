# coding=utf-8
import logging
from geosafe.tasks.headless.celery_app import app


__author__ = 'Rizky Maulana Nugraha <lana.pcfre@gmail.com>'
__date__ = '2/3/16'


LOGGER = logging.getLogger(__name__)


class RemoteTaskException(Exception):
    """Custom Exception for remote function.

    This exception will be raised if the function were executed directly,
    instead of using celery.
    """

    def __init__(self, *args, **kwargs):
        self.message = (
            'This function is intended to be executed by '
            'celery task remotely')
        super(RemoteTaskException, self).__init__(*args, **kwargs)


@app.task(
    name='headless.tasks.inasafe_wrapper.filter_impact_function',
    queue='inasafe-headless')
def filter_impact_function(hazard=None, exposure=None):
    """Filter available impact function for a given hazard and exposure.

    Proxy tasks for celery broker. It is not actually implemented here.
    It is implemented in InaSAFE headless.tasks package

    :param hazard: Hazard url path
    :type hazard: str

    :param exposure: Exposure url path
    :type exposure: str

    :return: The list of Impact Function ID
    :rtype: list(str)
    """
    raise RemoteTaskException()


@app.task(
    name='headless.tasks.inasafe_wrapper.run_analysis',
    queue='inasafe-headless-analysis')
def run_analysis(hazard, exposure, function, aggregation=None,
                 generate_report=False,
                 requested_extent=None,):
    """Run analysis with a given combination

    Proxy tasks for celery broker. It is not actually implemented here.
    It is implemented in InaSAFE headless.tasks package

    :param hazard: hazard layer url
    :type hazard: str

    :param exposure: exposure layer url
    :type exposure: str

    :param function: Impact Function ID of valid combination of
        hazard and exposure
    :type function: str

    :param aggregation: aggregation layer url
    :type aggregation: str

    :param generate_report: set True to generate pdf report
    :type generate_report: bool

    :param requested_extent: An extent of BBOX format list to denote the area
        of analysis
    :type requested_extent: list(float)

    :return: Impact layer url
    :rtype: str
    """
    raise RemoteTaskException()


@app.task(
    name='headless.tasks.inasafe_wrapper.read_keywords_iso_metadata',
    queue='inasafe-headless')
def read_keywords_iso_metadata(metadata_url, keyword=None):
    """Read keywords of a given metadata url.

    Proxy tasks for celery broker. It is not actually implemented here.
    It is implemented in InaSAFE headless.tasks package

    :param metadata_url: Metada url path
    :type metadata_url: str

    :param keyword: Requested keyword to query in metadata url
    :type keyword: str

    :return: return the whole keyword dictionary if keyword is None, return
        only the requested keyword key if given
    :rtype: dict, str
    """
    raise RemoteTaskException()
