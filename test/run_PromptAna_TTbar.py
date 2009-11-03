#

import FWCore.ParameterSet.Config as cms

process = cms.Process("test")
process.load("CondCore.DBCommon.CondDBSetup_cfi")

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("FWCore.MessageLogger.MessageLogger_cfi")

#
# DQM
#
process.load("DQMServices.Core.DQM_cfg")

process.load("DQMServices.Components.MEtoEDMConverter_cfi")

# HCALNoise module
## process.load("RecoMET.METProducers.hcalnoiseinfoproducer_cfi")
## process.hcalnoise.refillRefVectors = cms.bool(True)
## process.hcalnoise.hcalNoiseRBXCollName = "hcalnoise"
## process.hcalnoise.requirePedestals = cms.bool(False)

# the task - JetMET objects
#process.load("DQMOffline.JetMET.jetMETDQMOfflineSourceCosmic_cff")
process.load("DQMOffline.JetMET.jetMETDQMOfflineSource_cff")
process.jetMETAnalyzer.OutputMEsInRootFile = cms.bool(True)
process.jetMETAnalyzer.OutputFileName = cms.string('jetMETMonitoring_TTbar.root')
process.jetMETAnalyzer.TriggerResultsLabel = cms.InputTag("TriggerResults","","HLT8E29")
process.jetMETAnalyzer.processname = cms.string("HLT8E29")
process.jetMETAnalyzer.DoJetPtAnalysis = cms.untracked.bool(True)
process.jetMETAnalyzer.caloMETAnalysis.verbose = cms.int32(0)
process.jetMETAnalyzer.caloMETAnalysis.allSelection = cms.bool(True)
process.jetMETAnalyzer.caloMETNoHFAnalysis.allSelection = cms.bool(True)
process.jetMETAnalyzer.caloMETHOAnalysis.allSelection = cms.bool(True)
process.jetMETAnalyzer.caloMETNoHFHOAnalysis.allSelection = cms.bool(True)

# the task - JetMET trigger
#process.load("DQMOffline.Trigger.JetMETHLTOfflineSource_cfi")

# check # of bins
process.load("DQMServices.Components.DQMStoreStats_cfi")

# for igprof
#process.IgProfService = cms.Service("IgProfService",
#  reportFirstEvent            = cms.untracked.int32(0),
#  reportEventInterval         = cms.untracked.int32(25),
#  reportToFileAtPostEvent     = cms.untracked.string("| gzip -c > igdqm.%I.gz")
#)

#
#
# /TTbar/Summer09-MC_31X_V3-v1/GEN-SIM-RECO
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
   '/store/relval/CMSSW_3_4_0_pre1/RelValTTbar/GEN-SIM-RECO/MC_31X_V9-v1/0008/2C8CD8FE-B6B5-DE11-ACB8-001D09F2905B.root'

       )
)



#process.source.inputCommands = cms.untracked.vstring('keep *', 'drop *_MEtoEDMConverter_*_*')

process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32( 100 )
    input = cms.untracked.int32( 1000 )
)
process.Timing = cms.Service("Timing")

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('jetMETAnalyzer'),
    cout = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        jetMETAnalyzer = cms.untracked.PSet(
            limit = cms.untracked.int32(100)
        ),
        noLineBreaks = cms.untracked.bool(True),
        DEBUG = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        #FwkJob = cms.untracked.PSet(
        #    limit = cms.untracked.int32(0)
        #),
        threshold = cms.untracked.string('DEBUG')
    ),
    categories = cms.untracked.vstring('jetMETAnalyzer'),
    destinations = cms.untracked.vstring('cout')
)
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.FEVT = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('keep *_MEtoEDMConverter_*_*'),
    #outputCommands = cms.untracked.vstring('keep *'),
    fileName = cms.untracked.string('reco_DQM_TTbar.root')
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False) ## default is false

)

process.p = cms.Path(
    #process.hcalnoise *
         #             process.jetMETHLTOfflineSource*
                      process.jetMETDQMOfflineSource
#                    * process.jetMETDQMOfflineSourceCosmic
                     * process.MEtoEDMConverter
                     * process.dqmStoreStats)
process.outpath = cms.EndPath(process.FEVT)
process.DQM.collectorHost = ''

