#!/usr/bin/env python3
"""Deterministic Prompt 012 fixture generator. No network or repository writes."""
from __future__ import annotations
import copy, hashlib, json, re, sys
from typing import Any
import yaml

FRAMEWORK_REVISION='18335e57165a8984adab4790d3a6210355b484ba'
MISSION='verify-transition-recovery'; GOAL='recover-partial-lifecycle-transition'
EXEC='EX-20260729T050000Z-001'; PLAN='PERSIST-20260729T051000Z-001'
RECOVERY_PLAN='PERSIST-20260729T051500Z-001'; FINDING='FIND-930'; OP='chatgpt-session'
ROOT='.flywheel/operations/records/verify-transition-recovery/recover-partial-lifecycle-transition'
EXEC_PATH=f'{ROOT}/executions/{EXEC}.yaml'; STATE_PATH='.flywheel/state.yaml'
PLAN_PATH=f'{ROOT}/persistence/{PLAN}.yaml'; FINDING_PATH=f'{ROOT}/findings/{FINDING}.yaml'
RECOVERY_PLAN_PATH=f'{ROOT}/persistence/{RECOVERY_PLAN}.yaml'


def dump(value:dict[str,Any])->str:
    return yaml.safe_dump(value,sort_keys=False,allow_unicode=True,width=120).replace('\r\n','\n').replace('\r','\n').lstrip('\ufeff')
def sha(text:str)->str:return hashlib.sha256(text.encode()).hexdigest()
def blob(text:str)->str:
    raw=text.encode(); return hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest()
def snap(data:dict[str,Any])->dict[str,Any]:
    text=dump(data); return {'data':data,'yaml':text,'sha256':sha(text),'git_blob_sha':blob(text),'bytes':len(text.encode())}
def stage(status,started=None,completed=None,summary=None,refs=None,reason=None):
    return {'status':status,'started_at':started,'completed_at':completed,'summary':summary,'refs':refs or [],'reason':reason}

def mission():
    return {'schema_version':1,'id':MISSION,'title':'Verify Partial Lifecycle Transition Recovery','status':'active','objective':'Verify deterministic fresh-session recovery of a partial lifecycle transition.','constraints':['Synthetic read-only verification.'],'success_criteria':[{'id':'MSC-930','statement':'Recovery is deterministic and reproducible.'}],'goals':[GOAL],'approvals_required':[]}
def goal():
    statements=['Reconstruct durable transition intent.','Recognize the partial state.','Restore exact execution content.','Persist structured recovery evidence.','Finalize plans and continuation boundaries.','Reject invalid fixtures.','Preserve repository immutability.']
    criteria=[{'id':f'AC-{930+i}','statement':s} for i,s in enumerate(statements)]
    evidence=[{'criterion_id':c['id'],'evidence_types':['manual-verification']} for c in criteria]
    return {'schema_version':1,'id':GOAL,'mission_id':MISSION,'title':'Recover Partial Lifecycle Transition','status':'active','objective':'Verify exact non-persistent recovery.','depends_on':[],'blocked_by':[],'procedure':['Build fixtures.','Validate recovery.'],'acceptance_criteria':criteria,'evidence_required':evidence,'constraints':['Read-only.'],'approvals_required':[]}
def execution(classify:bool):
    lifecycle={
      'execute':stage('completed','2026-07-29T05:00:00Z','2026-07-29T05:03:00Z','Constructed fixtures.',['ACT-930']),
      'observe':stage('completed','2026-07-29T05:03:00Z','2026-07-29T05:07:00Z','Captured revisions.',['OBS-930']),
      'evaluate':stage('completed' if classify else 'in-progress','2026-07-29T05:07:00Z','2026-07-29T05:10:00Z' if classify else None,'Evaluation completed.' if classify else None,['EVAL-930']),
      'classify':stage('in-progress' if classify else 'pending','2026-07-29T05:10:00Z' if classify else None),
      'adapt':stage('pending'),'validate':stage('pending'),'persist':stage('pending'),'reuse':stage('pending')}
    return {'schema_version':1,'id':EXEC,'mission_id':MISSION,'goal_id':GOAL,'status':'in-progress','intended_outcome':'Verify deterministic partial-transition recovery.','acceptance_criteria':[f'AC-{i}' for i in range(930,937)],'started_at':'2026-07-29T05:00:00Z','completed_at':None,'lifecycle':lifecycle,'actions':['ACT-930: Construct deterministic fixtures.'],'observations':[{'id':'OBS-930','statement':'Retained execution and state agree.','type':'direct','status':'complete','observed_at':'2026-07-29T05:05:00Z','source_or_method':'Fixture inspection.','evidence_refs':['EVID-930'],'uncertainty':None,'conflicts_with':[]}],'evaluations':[{'id':'EVAL-930','statement':'The pair is transition-ready.','result':'supports','observation_refs':['OBS-930'],'evidence_refs':['EVID-930'],'criterion_refs':['AC-930','AC-931','AC-932'],'rule_refs':['TRANSITION-PLAN-001'],'limitations':['Synthetic only.'],'rationale':'All identities and lifecycle stages agree.'}],'classifications':[],'adaptations':[],'blockers':[],'approval_refs':[],'evidence_refs':['EVID-930'],'decision_refs':[],'finding_refs':[],'validation_results':[],'outcome':None,'completion':{'disposition':None,'rationale':None}}
def state(name:str):
    return {'schema_version':1,'phase':'operating','readiness':'ready-for-missions','status':'active','active_mission':MISSION,'active_goal':GOAL,'active_execution':EXEC,'lifecycle_stage':name,'implementation_available':True,'application_missions_allowed':True,'blockers':[],'last_durable_update':{'at':'2026-07-29T05:10:00Z' if name=='classify' else '2026-07-29T05:07:00Z','by':OP,'reason':f'Execution {EXEC} is at {name}.'}}
def plan(pre_e,pre_s,post_e,post_s):
    return {'schema_version':1,'id':PLAN,'mission_id':MISSION,'goal_id':GOAL,'execution_id':EXEC,'created_at':'2026-07-29T05:10:00Z','operator':OP,'status':'applying','targets':[{'id':'PT-001','artifact_type':'execution','path':EXEC_PATH,'operation':'update','mutability':'cas-update','dependency_refs':[],'expected_precondition':{'blob_sha':pre_e['git_blob_sha']},'proposed_content_digest':post_e['sha256'],'rollback':{'mode':'restore-retained-content','retained_content_digest':pre_e['sha256']}},{'id':'PT-002','artifact_type':'state','path':STATE_PATH,'operation':'update','mutability':'cas-update','dependency_refs':['PT-001'],'expected_precondition':{'blob_sha':pre_s['git_blob_sha']},'proposed_content_digest':post_s['sha256'],'rollback':{'mode':'restore-retained-content','retained_content_digest':pre_s['sha256']}}],'write_order':['PT-001','PT-002'],'recovery':{'mode':'not-started','finding_ref':None,'blocker':None},'final_verification':{'required':True,'verified_at':None,'result':'pending'}}
def finding(pre_e,pre_s,post_e,post_s):
    return {'schema_version':1,'id':FINDING,'kind':'finding','mission_id':MISSION,'goal_id':GOAL,'execution_id':EXEC,'created_at':'2026-07-29T05:15:00Z','created_by':OP,'summary':'Recovered a partial lifecycle transition.','status':'closed','classification':'repository-inconsistency','criterion_ids':['AC-931','AC-932','AC-933','AC-934'],'source_refs':[PLAN],'artifact_refs':[PLAN_PATH,EXEC_PATH,STATE_PATH],'evidence':None,'decision':None,'finding':{'finding_type':'partial-lifecycle-transition','description':'Execution write succeeded; state write did not occur; exact rollback restored the pair.','impact':'Classify remained transaction-pending.','discovered_at':'2026-07-29T05:15:00Z','disposition':'resolved','transition_recovery':{'original_plan_id':PLAN,'original_plan_path':PLAN_PATH,'transition_operator':OP,'transition_at':'2026-07-29T05:10:00Z','observed_at':'2026-07-29T05:15:00Z','targets':[{'target_id':'PT-001','artifact_type':'execution','path':EXEC_PATH,'operation':'update','retained_blob_sha':pre_e['git_blob_sha'],'retained_content_digest':pre_e['sha256'],'proposed_content_digest':post_e['sha256'],'observed_blob_sha':post_e['git_blob_sha'],'observed_content_digest':post_e['sha256'],'write_result':'succeeded','failure_detail':None},{'target_id':'PT-002','artifact_type':'state','path':STATE_PATH,'operation':'update','retained_blob_sha':pre_s['git_blob_sha'],'retained_content_digest':pre_s['sha256'],'proposed_content_digest':post_s['sha256'],'observed_blob_sha':pre_s['git_blob_sha'],'observed_content_digest':pre_s['sha256'],'write_result':'not-attempted','failure_detail':'Interrupted before state CAS.'}],'failure_condition':'Execution was written before interruption prevented state CAS.','rollback':{'attempted':True,'target_ids':['PT-001'],'result':'succeeded','restored_content_digest':pre_e['sha256'],'state_mutated':False,'detail':'Restored exact retained execution content by CAS.'},'original_pair_restored':True,'continuation_prohibited':True,'continuation_reason':'Plans and finding must be durable before lifecycle continuation.','recovery_action':'Finalize original plan rolled-back and create a new transition plan.','human_reconciliation_required':False}},'approval':None}
def recovery_plan(f):
    return {'schema_version':1,'id':RECOVERY_PLAN,'mission_id':MISSION,'goal_id':GOAL,'execution_id':EXEC,'created_at':'2026-07-29T05:15:00Z','operator':OP,'status':'applied','targets':[{'id':'PT-001','artifact_type':'finding','path':FINDING_PATH,'operation':'create','mutability':'create-only','dependency_refs':[],'expected_precondition':{'absence':True},'proposed_content_digest':f['sha256'],'rollback':{'mode':'delete-created','retained_content_digest':None}}],'write_order':['PT-001'],'recovery':{'mode':'not-started','finding_ref':None,'blocker':None},'final_verification':{'required':True,'verified_at':'2026-07-29T05:15:02Z','result':'passed'}}

def require(value:bool,message:str):
    if not value: raise AssertionError(message)
def schema_like_check(f:dict[str,Any]):
    p=f['finding']['transition_recovery']; required=['original_plan_id','original_plan_path','transition_operator','transition_at','observed_at','targets','failure_condition','rollback','original_pair_restored','continuation_prohibited','continuation_reason','recovery_action','human_reconciliation_required']
    require(all(k in p for k in required),'missing transition_recovery field'); require(p['continuation_prohibited'] is True,'continuation must be prohibited')
    require(any(t['write_result']=='succeeded' for t in p['targets']),'succeeded target required'); require(any(t['write_result'] in ('failed','not-attempted') for t in p['targets']),'failed/not-attempted target required')
    for t in p['targets']:
        for k in ['target_id','artifact_type','path','operation','retained_blob_sha','retained_content_digest','proposed_content_digest','observed_blob_sha','observed_content_digest','write_result','failure_detail']: require(k in t,f'missing {k}')
        if t['operation']=='update': require(t['retained_blob_sha'] and t['retained_content_digest'] and t['observed_blob_sha'] and t['observed_content_digest'],'update revision fields required')
        if t['write_result']=='succeeded': require(t['failure_detail'] is None and t['observed_blob_sha'] and t['observed_content_digest'],'successful target rules')
        else: require(bool(t['failure_detail']),'failure detail required')
    r=p['rollback']; require(all(k in r for k in ['attempted','target_ids','result','restored_content_digest','state_mutated','detail']),'rollback fields')
    if r['result']=='succeeded': require(r['restored_content_digest'] and r['state_mutated'] is False and p['original_pair_restored'] is True,'successful rollback rules')
    if p['original_pair_restored'] is False: require(p['human_reconciliation_required'] is True,'reconciliation required')
def invalid(base,change):
    v=copy.deepcopy(base); change(v)
    try:schema_like_check(v);return False
    except (AssertionError,KeyError):return True

def main():
    artifacts={}; artifacts['mission']=snap(mission()); artifacts['goal']=snap(goal()); artifacts['retained_execution']=snap(execution(False)); artifacts['retained_state']=snap(state('evaluate')); artifacts['proposed_execution']=snap(execution(True)); artifacts['proposed_state']=snap(state('classify'))
    artifacts['original_plan_applying']=snap(plan(artifacts['retained_execution'],artifacts['retained_state'],artifacts['proposed_execution'],artifacts['proposed_state']))
    artifacts['recovery_finding']=snap(finding(artifacts['retained_execution'],artifacts['retained_state'],artifacts['proposed_execution'],artifacts['proposed_state']))
    artifacts['recovery_plan_applied']=snap(recovery_plan(artifacts['recovery_finding']))
    final=copy.deepcopy(artifacts['original_plan_applying']['data']); final['status']='rolled-back'; final['recovery']={'mode':'exact-rollback','finding_ref':FINDING,'blocker':None}; final['final_verification']={'required':True,'verified_at':'2026-07-29T05:15:03Z','result':'passed'}; artifacts['original_plan_rolled_back']=snap(final)
    require(artifacts['retained_execution']['data']['lifecycle']['evaluate']['status']=='in-progress','retained execution'); require(artifacts['proposed_execution']['data']['lifecycle']['classify']['status']=='in-progress','proposed execution'); require(artifacts['original_plan_applying']['data']['write_order']==['PT-001','PT-002'],'plan order')
    f=artifacts['recovery_finding']['data']; schema_like_check(f); p=f['finding']['transition_recovery']; pts={t['target_id']:t for t in p['targets']}; plan_targets={t['id']:t for t in artifacts['original_plan_applying']['data']['targets']}
    require(p['original_plan_id']==PLAN and p['original_plan_path']==PLAN_PATH and set(pts)==set(plan_targets),'TRANSITION-FINDING-PLAN-001')
    for k in pts:
        require(pts[k]['path']==plan_targets[k]['path'] and pts[k]['operation']==plan_targets[k]['operation'] and pts[k]['retained_blob_sha']==plan_targets[k]['expected_precondition']['blob_sha'] and pts[k]['retained_content_digest']==plan_targets[k]['rollback']['retained_content_digest'] and pts[k]['proposed_content_digest']==plan_targets[k]['proposed_content_digest'],'TRANSITION-FINDING-PLAN-001')
    require(pts['PT-001']['observed_blob_sha']==artifacts['proposed_execution']['git_blob_sha'] and pts['PT-002']['observed_blob_sha']==artifacts['retained_state']['git_blob_sha'],'TRANSITION-FINDING-REVISION-001')
    require(pts['PT-001']['write_result']=='succeeded' and pts['PT-002']['write_result']=='not-attempted' and p['rollback']['result']=='succeeded' and p['original_pair_restored'] is True,'TRANSITION-FINDING-OUTCOME-001')
    cases={
      '16_missing_transition_recovery':invalid(f,lambda x:x['finding'].pop('transition_recovery')),
      '17_missing_required_field':invalid(f,lambda x:x['finding']['transition_recovery'].pop('failure_condition')),
      '18_missing_outcome_class':invalid(f,lambda x:[t.update({'write_result':'succeeded','failure_detail':None}) for t in x['finding']['transition_recovery']['targets']]),
      '19_missing_retained_revision':invalid(f,lambda x:x['finding']['transition_recovery']['targets'][0].update({'retained_blob_sha':None})),
      '20_invalid_success_observation':invalid(f,lambda x:x['finding']['transition_recovery']['targets'][0].update({'observed_blob_sha':None,'failure_detail':'bad'})),
      '21_missing_failure_detail':invalid(f,lambda x:x['finding']['transition_recovery']['targets'][1].update({'failure_detail':None})),
      '22_invalid_successful_rollback':invalid(f,lambda x:x['finding']['transition_recovery']['rollback'].update({'restored_content_digest':None,'state_mutated':True})),
      '23_unrestored_without_reconciliation':invalid(f,lambda x:x['finding']['transition_recovery'].update({'original_pair_restored':False,'human_reconciliation_required':False,'rollback':{'attempted':True,'target_ids':['PT-001'],'result':'failed','restored_content_digest':None,'state_mutated':False,'detail':'failed'}}))}
    require(all(cases.values()),'negative cases')
    report={'prompt':'012-recover-partial-lifecycle-transition','framework_revision':FRAMEWORK_REVISION,'normalization':'UTF-8, LF, no BOM','artifacts':{k:{x:v[x] for x in ['sha256','git_blob_sha','bytes','yaml']} for k,v in artifacts.items()},'checks':{'fixture_contracts':'passed','structured_recovery_schema_rules':'passed','TRANSITION-FINDING-PLAN-001':'passed','TRANSITION-FINDING-REVISION-001':'passed','TRANSITION-FINDING-OUTCOME-001':'passed'},'negative_cases_16_23':cases,'partial_state':{'classification':'execution written, state not written','execution_sha':artifacts['proposed_execution']['git_blob_sha'],'state_sha':artifacts['retained_state']['git_blob_sha']},'rollback':{'restored_execution_digest':artifacts['retained_execution']['sha256'],'state_mutated':False,'original_pair_restored':True},'result':'passed'}
    json.dump(report,sys.stdout,indent=2,sort_keys=True);sys.stdout.write('\n')
if __name__=='__main__':main()
