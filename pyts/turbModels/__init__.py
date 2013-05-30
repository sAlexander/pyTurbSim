import nwtc,iec,hydro
model_alias={
    'ieckai':iec.ieckai,
    'iecvkm':iec.iecvkm,
    'smooth':nwtc.smooth,
    'nwtcup':nwtc.nwtcup,
    'tidal':hydro.tidal,
    'river':hydro.river,
    }

def getModel(config,profModel):
    # return an instance of the appropriate model class:
    if '.' in config['TurbModel']:
        return eval(config['TurbModel'].lower()+'(profModel)')
    else:
        return model_alias[config['TurbModel'].lower()](profModel)
