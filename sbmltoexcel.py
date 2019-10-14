# encoding: utf-8

#input is sbml model and output-file' s name such as 'initialmdoel.xlsx'
def sbml_excel(modelname,output):
    from cobra.io.dict import model_to_dict, model_from_dict,metabolite_from_dict,gene_from_dict,reaction_from_dict
    from cobra.core import Model
    from cobra.io import read_sbml_model, write_sbml_model
    import pandas as pd
    model=read_sbml_model(modelname)
    a=model_to_dict(model,sort=False)
    #writer = pd.ExcelWriter(modelname[:-4]+'.xlsx')
    writer = pd.ExcelWriter(output)
    #pd.DataFrame(a['compartments']).to_excel(writer,'Sheet1',index=False)
    pd.DataFrame(a['metabolites']).to_excel(writer,'metabolites',index=False)
    pd.DataFrame(a['genes']).to_excel(writer,'genes',index=False)
    df_r=pd.DataFrame(a['reactions'])
    df_r['reaction_eq'] = df_r.id.apply(lambda x: model.reactions.get_by_id(x).build_reaction_string(use_metabolite_names=False))
    df_r['reaction_eq_name'] = df_r.id.apply(lambda x: model.reactions.get_by_id(x).build_reaction_string(use_metabolite_names=True))
    #del df_r['metabolites'] #生成反应方程列后将代谢物列删除，可保留以方便再次读取
    df_r.to_excel(writer,'reactions',index=False)
    #df_r.to_excel(writer,'reactions',columns=["id","name","reaction","lower_bound","upper_bound","gene_reaction_rule"],index=False)
    writer.save()


#input is cobrapy model and out
def model_excel(model,output):
    from cobra.io.dict import model_to_dict, model_from_dict,metabolite_from_dict,gene_from_dict,reaction_from_dict
    from cobra.core import Model
    from cobra.io import read_sbml_model, write_sbml_model
    import pandas as pd
    a=model_to_dict(model,sort=False)
    writer = pd.ExcelWriter(output)
    #pd.DataFrame(a['compartments']).to_excel(writer,'Sheet1',index=False)
    pd.DataFrame(a['metabolites']).to_excel(writer,'metabolites',index=False)
    pd.DataFrame(a['genes']).to_excel(writer,'genes',index=False)
    df_r=pd.DataFrame(a['reactions'])
    df_r['reaction_eq'] = df_r.id.apply(lambda x: model.reactions.get_by_id(x).build_reaction_string(use_metabolite_names=False))
    #del df_r['metabolites'] #生成反应方程列后将代谢物列删除，可保留以方便再次读取
    df_r.to_excel(writer,'reactions',index=False)
    #df_r.to_excel(writer,'reactions',columns=["id","name","reaction","lower_bound","upper_bound","gene_reaction_rule"],index=False)
    writer.save()
#if __name__ == "__main__":
    #sbml_excel(modelname)