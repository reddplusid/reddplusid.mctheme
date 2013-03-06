from collective.grok import gs
from reddplusid.mctheme import MessageFactory as _

@gs.importstep(
    name=u'reddplusid.mctheme', 
    title=_('reddplusid.mctheme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('reddplusid.mctheme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
