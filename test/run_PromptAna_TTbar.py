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
process.load("RecoMET.METProducers.hcalnoiseinfoproducer_cfi")
process.hcalnoise.refillRefVectors = cms.bool(True)
process.hcalnoise.hcalNoiseRBXCollName = "hcalnoise"
process.hcalnoise.requirePedestals = cms.bool(False)

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
process.load("DQMOffline.Trigger.JetMETHLTOfflineSource_cfi")

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
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0026/E01614FB-6C89-DE11-8089-003048C57816.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0026/DEC94FF2-1D8B-DE11-A686-003048C5750A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0026/C62CBBB6-EB88-DE11-B14E-0019BBEBB54A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0026/B826FAFB-378B-DE11-A935-0018FEFAA390.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0026/A8503D27-1189-DE11-A144-0018FEFAA3C6.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0026/9AB3304B-6D89-DE11-AEB7-0019BBEBF5B4.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0026/86EE1F02-6E89-DE11-BEEF-00144F0F621E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0026/8083DF31-6D89-DE11-A3A6-001E682F8B72.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0026/7AFF5898-9E89-DE11-B633-001F29C8CCCC.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0026/725DAA2C-8189-DE11-BF39-0030487CAA53.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0026/5E48EEBB-F088-DE11-A59F-001CC4BEAA0C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0026/4E3AAAB0-0B8B-DE11-97A5-003048C56D1A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0026/42E42891-FC88-DE11-AE90-000E0C6A922B.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0026/10B981F7-F488-DE11-8278-001E680F7D1C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/FC68D9F3-A588-DE11-842D-0030487B442C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/FADB6D62-AF88-DE11-ACEA-003048C5780E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/FAC3FAF4-6B88-DE11-9B23-00215E21D894.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/F89135DC-BE88-DE11-A81F-0018FEFAC3C4.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/F87056E2-5E88-DE11-90AD-003048945390.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/F475FD35-A988-DE11-A933-001F29C9E49E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/F0E380AF-AB88-DE11-A283-00163691DD05.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/F0A751B7-6488-DE11-BD97-00215E21D948.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/F0203C95-D788-DE11-83EE-001CC4BD73F0.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/EAB08E02-A788-DE11-8B8A-0019BBEBD69A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/E6F63435-A588-DE11-9B0D-0016366DB30E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/E6346D7D-3288-DE11-A357-003048792C0E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/E4CF88B4-A588-DE11-BB89-001E68A9941C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/E0FEDE97-A588-DE11-97D7-0016368E0F5F.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/E0D85530-3588-DE11-B1B6-003048C5750A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/DEC6EE43-CE88-DE11-AB94-001CC4BF9C1E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/DE94FDC1-A588-DE11-AB21-001E682F882A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/DE718FBC-6488-DE11-98A9-00215E21DBD0.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/DE5A02D1-BC88-DE11-A880-001CC4BE553E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/DCC8D1A3-B388-DE11-A2B0-0019BBEBB558.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/DCB0BFE5-D288-DE11-BC01-0019BBEB551A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/DAED3FAE-CC88-DE11-AFDF-001CC4BE374C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/DA38DDD8-A588-DE11-8DF0-001E6837DC54.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/DA1AD644-A588-DE11-BE04-001E682F882A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/DA03D025-6E88-DE11-AF9B-00304894539C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/D8F089FC-A688-DE11-8AAA-0018FEFAA3FE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/D8B5D27C-6E88-DE11-B333-001F29C9A5AE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/D8069195-A588-DE11-ABCD-0030487C6F54.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/D6DBDE79-C388-DE11-AF3B-001CC4BF9C1E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/D2279A4B-7188-DE11-B0FB-001F29C9E49E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/D0A6AEDB-9A88-DE11-BD7E-001CC4BE75AC.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/D0717102-A588-DE11-B631-001E682F84DE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/D010CFC3-6488-DE11-9BFA-0030489454B8.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/CE8FD7DF-A488-DE11-9B3C-0016368E0C93.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/CE2016AB-A588-DE11-9F08-001636847653.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/CCFFDA4F-DC88-DE11-A056-001CC4BFBC0C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/CCD01369-6988-DE11-BCE6-003048C57484.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/CC772955-C588-DE11-90E1-001A4B0A27B0.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/CC699105-7088-DE11-8CE5-001F29C9653E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/CADF708D-6C88-DE11-8B44-003048976AF6.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/CAAD036F-9D88-DE11-B2EF-0019BBEBE520.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/C6D5EC5C-AC88-DE11-B7B9-00144F015C2A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/C428A8D5-A988-DE11-AB59-001E6837DFEA.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/C4218723-9D88-DE11-9D4B-0018FEFAB6BC.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/C23347D3-9A88-DE11-934D-001A4B0A2850.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/C0C97B07-E488-DE11-B68A-001CC4BE374C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/C0C117E5-A988-DE11-9378-00163691DD05.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/C0099572-7A88-DE11-A31A-001F29C89EA2.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/C0038A90-A988-DE11-B0F8-00304879FB84.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/BED029AF-6188-DE11-A1FD-003048C56E54.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/BAD74C36-7888-DE11-8214-001F29C7BDEE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/B6FD6A6C-6688-DE11-BA84-003048976B12.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/B484CE79-C088-DE11-BE7A-001A4BD01A60.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/B2D630B2-DA88-DE11-B15B-001CC4BF9C1E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/B233EAE5-A988-DE11-B034-00163691DD05.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/B2317F4D-DC88-DE11-9241-001CC4BE0A46.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/B06E55CD-A588-DE11-9237-0016368E0B47.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/B02B32B6-6488-DE11-8F3A-00215E220918.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/B01D7F3B-AA88-DE11-9882-0030487C6F54.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/AEC84B35-A988-DE11-AD3B-001F29C9C492.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/AE8AA03B-B488-DE11-8033-0019BBEBF61E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/AE89776D-6688-DE11-ACE7-003048C6D558.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/A616D99F-9D88-DE11-913B-0019BBEB54D6.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/A2FD4C2A-6788-DE11-B820-00215E21DF96.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/A0FEB041-A688-DE11-BDF1-0019BBEBB634.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/9E80A46A-AA88-DE11-94BD-001E682F882A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/9E21207A-5B88-DE11-A082-003048943EBC.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/9AFE2F9D-A988-DE11-90C0-001E68A9941C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/9A3A1325-CB88-DE11-B8B5-001CC4BE7702.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/985797CC-CF88-DE11-A096-001CC442D324.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/96FF15CB-CF88-DE11-9708-001CC4BD73F0.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/96A5B27C-6388-DE11-B406-001F29C89EA2.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/960BF0D6-3388-DE11-9160-001F29C9A546.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/92E9F12B-3588-DE11-91E2-003048792CD0.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/923F3712-D688-DE11-92CE-001CC4BF482A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/8E0E480D-7888-DE11-93A9-001F29C9E49E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/8CFCC401-9D88-DE11-AE78-001A4B0A3586.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/8CACB597-3988-DE11-99BE-003048982851.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/8ACB8A27-6788-DE11-A93F-00215E21D894.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/8A4F23C6-C988-DE11-A3E6-001CC4BD73F0.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/8A39397C-6988-DE11-970D-003048C6D558.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/8A30BFC2-A588-DE11-838E-0030487B44EE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/88C1D3DD-6988-DE11-B9BD-001F29C79C66.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/883C9E06-BA88-DE11-A06D-0019BBEBF61E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/86F2D4EF-A488-DE11-AB9A-001E6837DC54.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/86148286-C688-DE11-A08F-001CC4BFD912.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/84548DF1-6788-DE11-8C9B-003048C56D6C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/822F082E-A588-DE11-BBAC-0018F3E66128.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/822C0CF3-6B88-DE11-AF7F-00215E22237C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/822ACDD7-A488-DE11-AB09-001E682F8578.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/80074AE9-8688-DE11-9E24-0030487CAA53.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/7E95661F-9E88-DE11-BE40-001CC4BF8CE4.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/7E5E415C-6388-DE11-9BF0-003048C6B516.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/78EF9DF5-A588-DE11-A765-0018FEFAA3AC.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/7850499E-A588-DE11-85A5-001E68A994C6.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/78084AA1-6C88-DE11-BDB2-003048792C14.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/7636FB0C-A688-DE11-A7DE-0030487B44EE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/74AACFFC-A688-DE11-A195-001A4B0A3436.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/74489C3C-D988-DE11-B186-001CC4BF482A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/70E07272-7A88-DE11-B4ED-001F29C89EA2.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/70B05DB0-CC88-DE11-BE70-001B78E190F0.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/7040D83E-9D88-DE11-8D86-0018FEFAC3FA.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/6E868C9D-A588-DE11-8C0A-0030487CF41C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/6CEC402D-6788-DE11-A209-00215E2227F0.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/6AC5BBE9-C188-DE11-816F-001A4B0A2764.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/6A5D3EB4-6488-DE11-B7DC-00215E22185A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/68EC9AEE-EA88-DE11-AED2-000E0C3CE775.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/68B44FC6-6488-DE11-BB8B-003048C57344.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/681E41DF-9A88-DE11-BA98-0019BBEBE520.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/66EEEC3B-BF88-DE11-8128-001CC4BED9DC.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/66AD1873-7A88-DE11-ADB5-001F29C89EA2.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/66ACE929-6788-DE11-A905-00215E221818.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/662AE7C7-A288-DE11-888F-003048C56E84.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/64E054EC-ED88-DE11-B168-000E0C6A92A1.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/646627DC-6988-DE11-8941-001F29C945FE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/622B8A2F-AA88-DE11-A762-001E68A996EA.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/62291042-B488-DE11-A7D5-001E6849DC22.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/60E4F6FA-DD88-DE11-A0C4-001CC4BF767A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/6004FF4C-AA88-DE11-B0BF-001E68A9941C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/5E892303-A788-DE11-B9C6-001CC4BE0A46.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/5E26F302-6888-DE11-97E8-003048C6B548.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/5CD5F0AB-9B88-DE11-A8A6-001A4B0A3490.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/5C7A8C5A-AC88-DE11-94EB-001F29C9C492.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/5A5036A8-E588-DE11-98E1-001A4B0A0602.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/5A2FDF1E-6088-DE11-B33A-003048976ACA.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/58968FD8-5E88-DE11-B451-003048976ACA.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/54F1370A-BF88-DE11-ACA9-001CC4BF8C40.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/54CC7EE9-A988-DE11-9666-001E68A993F4.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/548F6026-6E88-DE11-A524-001F29C7BDEE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/5478A829-CB88-DE11-A477-001CC4BF8C60.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/524BE55C-DF88-DE11-B7EB-0018FEFAA3F0.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/50AABE8C-9C88-DE11-A3CA-001CC4BE7702.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/4C208A84-3588-DE11-96EE-001F29C9C5A8.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/4A60EFD0-5E88-DE11-A58B-003048C56C0C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/4A1421DC-9A88-DE11-88D0-0019BBEBC210.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/48AC6C31-AA88-DE11-B02C-0030487C6F54.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/4437FBAA-7588-DE11-95C5-00215E221782.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/42EAF2B8-A588-DE11-997B-00163691DD05.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/429AEDA7-6188-DE11-A8C6-003048976C42.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/42881F4C-A788-DE11-9446-00304879FB84.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/40E7F510-A588-DE11-8AAE-0030487B44EE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/40C5B600-9E88-DE11-8C02-001CC4BF9C5C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/40AA97DE-7288-DE11-85F9-001F29C9E49E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/403D5B03-A788-DE11-BE40-001CC4BF8694.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/3EC1A90E-7688-DE11-9161-001F29C9E49E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/3EBF3FEA-DD88-DE11-A156-001A4B0A345C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/3E95F881-C688-DE11-87CC-001CC4BF57C6.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/3E426D11-6B88-DE11-BD01-003048C6D558.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/3E2ED748-BF88-DE11-A266-001CC4BE55CA.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/3E2400E7-C588-DE11-BC17-0019BBEB54B6.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/3C5F0B0B-B888-DE11-B17E-001CC4BD73F0.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/3C22EA11-A688-DE11-A8E0-001E682F8B72.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/3AB33C24-CB88-DE11-A849-001CC4BF9C5C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/38E94E18-E188-DE11-BE6F-0018FEFAC3B6.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/389E0005-A788-DE11-BD5C-0019BBEBF550.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/3407E948-9D88-DE11-8D53-001CC4BF1D2C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/32FA49FD-5F88-DE11-9D0C-00215E220918.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/30E55643-CE88-DE11-A324-001CC4BF482A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/30635F3E-D988-DE11-82F6-001CC4BEAA0C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/3044EC70-A788-DE11-9055-003048C56E84.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/302AEF61-3288-DE11-8172-003048792CC2.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/301531F4-A988-DE11-BF4E-001E68A996EA.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/3008AF1E-A588-DE11-B4E8-00163691DBF9.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/2ECA5D74-A988-DE11-92E4-003048C56FCE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/2E561230-7688-DE11-A547-001F29C89EA2.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/2C81EF8A-BA88-DE11-AB74-001CC4BF9C1E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/2AD06517-9D88-DE11-B01B-001CC442D324.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/28D768A1-C988-DE11-8EEA-001CC4BF6F3A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/28BA8D3F-3388-DE11-BE36-001F29C7BDEE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/286268FD-9C88-DE11-A115-001A4B0A2788.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/284EDCF0-6788-DE11-92E1-003048C6B52A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/28300F74-5288-DE11-9882-003048C56C0C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/26550DEB-A588-DE11-90A5-001B249329B4.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/262B48BC-A588-DE11-8961-0016368E0B47.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/24BDE82E-7688-DE11-8C72-001F29C9A5CA.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/22B69581-7A88-DE11-94B3-001F29C9C5C4.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/1E3C51C0-3588-DE11-9AC1-001F29C7DA02.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/18FABAC1-BC88-DE11-AE09-001CC4BF9C5C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/182B8EDE-6988-DE11-AA6F-001F29C9653E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/168E3570-7A88-DE11-A9D6-001F29C82C60.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/12DA72FA-A688-DE11-B7B1-0018FEFAC396.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/129A0B85-AA88-DE11-B08A-001E6837DFEA.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/125D28B3-3388-DE11-A1C8-001F29C9950E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/104EF829-6788-DE11-BB86-00215E221BC0.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/0EEFF074-9D88-DE11-8873-0018FEFAA374.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/0E84521E-9E88-DE11-BF3A-001CC4BF57C6.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/0E5F87CE-3388-DE11-9B7D-001F29C7DA02.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/0C7B38EB-D288-DE11-AEF8-001CC4BF9C1E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/08B8C35C-A788-DE11-AD2F-00304879FBFA.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/06EA3C6D-6688-DE11-B598-0030489454B8.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/06D4D3AC-AA88-DE11-8084-00215E21F214.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/06BA21F7-A988-DE11-9FEB-00304879FBFA.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/040B91BA-6488-DE11-9D27-00215E221BC0.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0025/02D14027-6B88-DE11-BD82-003048C56FCE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/FE8CFDCF-2F88-DE11-A502-001F29C9D4A8.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/FA45B1B2-1B88-DE11-9DCF-00215E222262.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/F6BAF466-2188-DE11-A288-00304894566E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/F6B7897A-9E88-DE11-8E7D-001A4B0A2786.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/F6998291-2F88-DE11-B30F-001F29C96530.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/EEB25E6D-2F88-DE11-A9D4-001F29C6E900.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/EE42477F-2788-DE11-8B70-0015171A4660.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/EE1EF3DE-3088-DE11-80A9-001F29C7BDEE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/EA9EFC25-3288-DE11-B785-001F29C9A5CA.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/EA0382E7-2B88-DE11-91DF-0030489455FE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/E4BFCBCB-1F88-DE11-88AB-003048976C42.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/E492CEF2-2288-DE11-B791-003048976C42.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/E2CFAAAE-2C88-DE11-B0A0-001F29C7BDEE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/E21FCCF7-1C88-DE11-BD00-00215E21DD32.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/E20A9531-1B88-DE11-8E90-003048976B48.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/E20060FD-2988-DE11-B465-0030488E6260.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/DA6CD0F4-1C88-DE11-A44E-00215E21DD68.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/DA4FE0D1-1F88-DE11-B667-0030489454FE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/D646AFFA-2F88-DE11-A143-001F29C9C5C4.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/D4BDA140-2D88-DE11-BEF0-001F29C7BD6C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/D4833BED-2588-DE11-BBDC-00304894566E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/D4354CB3-2488-DE11-92FD-00215E222382.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/D2C2D16B-2488-DE11-8978-003048976AE4.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/D26BFEDB-1F88-DE11-BF3B-003048C57352.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/D00A0B26-1D88-DE11-8003-003048C57358.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/CAC25470-2788-DE11-A55F-0019BBEB5552.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/CA3FF0D2-1F88-DE11-B57B-0030489454A2.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/CA0F00EC-2B88-DE11-810A-003048945430.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/C8ABF9BA-1988-DE11-8B6F-00215E222256.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/C81F98DF-2388-DE11-857A-00215E21DC72.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/C6E145FB-3088-DE11-A0C8-001F29C88B2C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/C692DD09-2088-DE11-B280-00215E21DC7E.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/C0F8B4F3-1C88-DE11-9600-00215E222262.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/C04A846E-9E88-DE11-91C2-001A4B0A06D0.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/BC66BB19-1D88-DE11-AC11-00215E21D69C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/B85E9F19-3188-DE11-BDA5-001F29C9C5CE.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/B6BE9DF8-2288-DE11-B5F6-003048C6B4E4.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/B6AC5884-B188-DE11-8F72-0019BBEBD32C.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/B4800CD6-1B88-DE11-AC36-00215E22200A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/B03C075F-2188-DE11-B6FB-003048C5730A.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/ACE939EC-9988-DE11-B871-001A4B0A35B2.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/A8B62584-B188-DE11-8D35-0019BBEBB5B8.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/A889202A-2088-DE11-8589-00215E21D786.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/A4FFAFF4-1C88-DE11-A039-00215E221FDA.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/A4B904FB-1B88-DE11-8E90-00215E21DAC8.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/A083D5EC-2988-DE11-BFC7-003048C574A8.root',
              '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/A04E071C-2688-DE11-A2BA-00215E21D732.root'
       )
)

#           '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/9E552719-1D88-DE11-9E9F-00215E2223D6.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/9E10832E-1E88-DE11-A2BB-00304894532C.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/9CB3775C-1E88-DE11-AAD0-00215E21D8E2.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/98EA8CD5-1B88-DE11-AD84-00215E21DD32.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/9689DA75-2C88-DE11-BF14-001F29C7DA02.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/960C9D61-1E88-DE11-B94F-00215E221158.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/94273461-1E88-DE11-B402-00215E21E1C4.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/929C399A-3088-DE11-AB39-001F29C7BDEE.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/926D60DA-2588-DE11-8F6E-003048976C7A.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/920D2DE6-2F88-DE11-A1FD-001F29C8CCCC.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/906AB1DA-1F88-DE11-977A-003048976AD8.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/8EFA04DB-1F88-DE11-879D-0030489453EC.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/8E9D6560-3288-DE11-B33D-0030487CA7E5.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/8E23BE56-2188-DE11-9C00-003048943EBC.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/8C9204E1-1F88-DE11-B12E-003048976AE4.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/8AC41793-1B88-DE11-89A7-00215E21DD68.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/883BBA57-2188-DE11-A264-003048C6B578.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/7E962D1D-2E88-DE11-8482-001F29C9C5A8.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/7C81F6E5-2B88-DE11-9FFB-003048C56E68.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/745D23A2-2D88-DE11-9970-003048C57348.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/724EFEA2-1C88-DE11-865A-0030489454B8.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/702871A7-2788-DE11-850C-00215E21D9AE.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/6CF0F573-3088-DE11-A529-001F29C82C60.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/6CA1C7BD-5988-DE11-940A-001A4B0A35F6.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/6ADBFEC6-2788-DE11-9160-00215E21DD50.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/6A04CDDB-2588-DE11-B5F0-003048C6D56A.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/68B73E2F-1E88-DE11-B651-003048C6B4E4.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/66968031-1B88-DE11-91C7-003048945616.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/6653DAC7-2788-DE11-8A47-00215E22158A.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/62781CBB-3088-DE11-8BDE-001F29C9950E.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/605296DF-2388-DE11-9569-00215E221218.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/60395456-2188-DE11-8E55-00304896B952.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/5A7405BC-2F88-DE11-8235-001F29C9C5CE.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/5A6A0074-2788-DE11-85E5-003048C574A8.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/58AA7EB8-1C88-DE11-993F-003048C6B50E.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/5811A607-3088-DE11-A1E2-001F29C9C5CE.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/52BC649C-1988-DE11-8867-003048976C42.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/5031021A-1D88-DE11-BC5F-00215E220F78.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/5022FE0B-2088-DE11-ABFD-00215E22223E.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/4E89D491-3188-DE11-8DA4-001F29C89EA2.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/4CC63E07-3088-DE11-8301-001F29C7BDEE.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/4C1C22C7-3188-DE11-9588-001F29C9A5CA.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/4A2C6160-1E88-DE11-91CE-00215E221182.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/46D63D26-3088-DE11-A74C-001F29C9C5A8.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/46C4F20B-2088-DE11-A0AE-00215E2222E0.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/46B65E9D-1C88-DE11-AA6D-003048976ACA.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/467FADD6-1B88-DE11-9E67-00215E21DB88.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/409B496C-2488-DE11-B9A5-003048C57460.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/3E680B19-1D88-DE11-9825-00215E221FB0.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/3E01A10F-2A88-DE11-963F-003048C6D56A.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/38F2ACC5-2788-DE11-9931-00215E21DAC8.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/36B211DF-2788-DE11-A642-00215E2217CA.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/368517DC-1F88-DE11-852F-003048C6D56A.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/32150B6F-3088-DE11-8849-001F29C6E900.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/2E089F6B-B088-DE11-8BC1-001A4B0A360C.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/2C79CB6B-2488-DE11-906D-00304894532C.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/2A4A11BA-2F88-DE11-AF2A-001F29C9E49E.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/2A2B2F5E-2D88-DE11-8547-003048C574A8.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/280C7CB2-1B88-DE11-A3F0-00215E2213EC.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/26F4E960-1E88-DE11-88DE-00215E2223D6.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/2244286C-2488-DE11-B184-003048C6B578.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/20F10C1C-2688-DE11-BD04-00215E2222C2.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/18336E94-2188-DE11-A54A-00215E21F32E.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/169B8EB5-B088-DE11-8BAD-001A4B0A28B6.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/14D1B818-3188-DE11-8B57-001F29C9C492.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/102C0EF4-1C88-DE11-9838-00215E221794.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/0CAA279D-1C88-DE11-B547-0030489453EC.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/0A975EB3-1B88-DE11-8BD8-00215E222760.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/0A328BFD-2288-DE11-9316-003048976B40.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/067C3E72-3288-DE11-9B2D-003048982851.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/061F8D86-2788-DE11-8860-0019BBEBD6B2.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/04567A2D-2C88-DE11-ABE5-001F29C9950E.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/0248F554-3088-DE11-8D00-001F29C79C66.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/00D420F9-2B88-DE11-A133-003048C56E14.root',
#                  '/store/mc/Summer09/TTbar/GEN-SIM-RECO/MC_31X_V3-v1/0024/00A3FFB4-3088-DE11-8CAD-003048C56E14.root'

process.source.inputCommands = cms.untracked.vstring('keep *', 'drop *_MEtoEDMConverter_*_*')

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
    wantSummary = cms.untracked.bool(True) ## default is false

)

process.p = cms.Path(process.hcalnoise
                     * process.jetMETHLTOfflineSource
                     * process.jetMETDQMOfflineSource
#                    * process.jetMETDQMOfflineSourceCosmic
                     * process.MEtoEDMConverter
                     * process.dqmStoreStats)
process.outpath = cms.EndPath(process.FEVT)
process.DQM.collectorHost = ''

