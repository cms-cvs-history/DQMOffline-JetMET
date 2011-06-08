#include <iostream>

#include "DQMOffline/JetMET/plugins/SusyPostProcessor.h"
#include "DQMOffline/JetMET/interface/SusyDQM/Quantile.h"
#include "FWCore/PluginManager/interface/ModuleDef.h"

using namespace std;

SusyPostProcessor::SusyPostProcessor(const edm::ParameterSet& pSet)
{
  
  dqm = 0;
  dqm = edm::Service<DQMStore>().operator->();
  iConfig = pSet;

  SUSYFolder = iConfig.getParameter<string>("folderName");

}

SusyPostProcessor::~SusyPostProcessor(){
}

void SusyPostProcessor::beginJob(void){
}

void SusyPostProcessor::beginRun(const edm::Run&, const edm::EventSetup& iSetup){
}

void SusyPostProcessor::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup){
}

void  SusyPostProcessor::QuantilePlots(MonitorElement* ME, double q_value)
{
  if(ME->getTH1()->GetEntries()>0.)
    {
      Quantile q(static_cast<const TH1*>(ME->getTH1()));
      Float_t mean=q[q_value].first;
      Float_t RMS=q[q_value].second;
      
      Float_t xLow=-5.5;
      Float_t xUp=9.5;
      Int_t NBin=15;
      
      if(mean>0.)
	{
	  Float_t DBin=RMS*TMath::Sqrt(12.)/2.;
	  xLow=mean-int(mean/DBin+2)*DBin;
	  xUp=int(0.2*mean/DBin)*DBin+mean+5*DBin;
	  NBin=(xUp-xLow)/DBin;
	}

      dqm->setCurrentFolder(ME->getPathname());
      TString name=ME->getTH1()->GetName();
      name+="_quant";
      //std::cout<<name<<std::endl;
      ME=dqm->book1D(name,"",NBin, xLow, xUp);
      ME->Fill(mean-RMS);
      ME->Fill(mean+RMS);
    }
}



void SusyPostProcessor::endRun(const edm::Run&, const edm::EventSetup&)
{
  //std::cout<<"here 1"<<std::endl;
  dqm->setCurrentFolder(SUSYFolder);
  Dirs = dqm->getSubdirs();
  for (int i=0; i<int(Dirs.size()); i++)
    {
      //std::cout<<Dirs[i]<<std::endl;
      size_t found = Dirs[i].find("Alpha");
      if (found!=string::npos) continue;
      //std::cout<<string::npos<<std::endl;
      if(!dqm->dirExists(Dirs[i])){
	cout << "Directory "<<Dirs[i]<<" doesn't exist!!" << std::endl;
	continue;
      }
      
      vector<MonitorElement*> histoVector = dqm->getContents(Dirs[i]);

      for (int i=0; i<int(histoVector.size()); i++) {
	std::cout<<histoVector[i]->getTH1()->GetName()<<std::endl;
	QuantilePlots(histoVector[i],0.05);
      } 
    }
}


void SusyPostProcessor::endJob(){}





