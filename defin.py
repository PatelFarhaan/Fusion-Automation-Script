
package_names = [
'oracle_fusion_fundamentals_training',
'fusion_hcm_core_training',
'oracle_fusion_talent_management_training',
'oracle_fusion_benefits_training_1',
'oracle_fusion_benefits_training_2',
'fusion_payroll_training',
'oracle_fusion_fastformula',
'oracle_fusion_compensation_workbench',
'oracle_fusion_hcm_approval_management',
'oracle_fusion_time_and_labour_training',
'fusion_hcm_for_ebs_hcm_experts_training',
'fusion_procurement_training',
'oracle_fusion_hcm_technical_training',
'oracle_fusion_financials_accounting_hub_training_1',
'oracle_fusion_financials_accounting_hub_training_2',
'oracle_fusion_procure_to_pay_training',
'fusion_application_installation_and_patching_R9_training',
'development_in_fusion_applications',
'oracle_fusion_financials_training',
'oracle_BI_reproting_and_OTBI_training_in_fusion_apps_1',
'oracle_BI_reproting_and_OTBI_training_in_fusion_apps_2',
'oracle_fusion_accounts_receivable_training',
'oracle_fusion_financials_cloud_tax_training',
'oracle_apps_DBA',
'oracle_EBS_R12_inventory_order_management_and_purchasing_training',
'oracle_R12_subledger_accounting_training',
'oracle_EBS_R12_functional_financial_training',
'OA_framework_training',
'R12_advanced_global_intercompany_system_AGIS_training',
'oracle_EBusiness_tax_training_1',
'oracle_EBusiness_tax_training_2',
'oracle_demantra_training',
'oracle_R12_HRMS_payroll_training',
'oracle_implement_configurator_training',
'oracle_R12_project_accounting_training',
'oracle_R12_advance_supply_chain_planning_training',
'oracle_R12_financial_accounting_hub_training',
'oracle_business_intelligence_applications_training',
'oracle_business_intelligence_enterprise_edition_training',
'oracle_adf_training',
'oracle_business_process_management_training',
'oracle_soa_BPEL_mediator_OBS_development_training_1',
'oracle_soa_BPEL_mediator_OBS_development_training_12C',
'oracle_data_integrator_training',
'oracle_mobile_application_framework_training',
'oracle_java_xml_and_web_service_training',
'oracle_sql_and_plSQL_training',
'fusion_financials_integration_training',
'fusion_financials_security_training_1',
'fusion_financials_security_training_2',
'fusion_financials_reporting_training',
'fusion_financials_approval_management_training',
'oracle_fusion_integration_cloud_Service_training',
'oracle_sales_cloud_extensibility_training',
'oracle_fusion_account_payable_training',
'oracle_fusion_general_ledger_training',
'fusion_fixed_asset_training',
'oracle_fusion_project_portfolio_management_training',
'oracle_business_suit_fundamentals_training',
'oracle_R12_iprocurement_training',
'oracle_ebs_R12_service_contract_training',
'oracle_ebs_R12_fixed_assets_training',
'oracle_transportation_management_training',
'oracle_demantra_ptp_training',
'oracle_identity_management_training',
'oracle_access_manager_training',
'oracle_weblogic_administrator_training',
'oracle_entitlement_server_training',
'fusion_middleware_12C_training',
'oracle_goldengate_training',
'oracle_database_12C_advanced_admininstration_training',
'oracle_data_guard_administration_training',
'r12_approval_management_training_1',
'ebusiness_suit_development_erp_training',
'workflow_training',
'bi_publisher_training',
'ebs_techno_functional_training',
'fusion_hcm_reporting_training',
'oracle_fusion_hcm_integration_training',
'fusion_security_training',
'oracle_taleo_recruting_and_onboarding_training',
'oracle_taleo_tcc_training',
'oracle_taleo_integration_training',
'r12_approval_management_training_2',
'r1213_administration_training',
'Siebel_openUI_training',
'hyperion_financials_management_hfm_training',
'hyperion_planning_training',
'mastering_hyperion_calculation_manager'

]


xpath = [

'44',
'35',
'30',
'64',
'283',
'239',
'45',
'29',
'240',
'241',
'245',
'39',
'277',
'259',
'46',
'62',
'115',
'83',
'50',
'123',
'135',
'229',
'256',
'145',
'49',
'43',
'117',
'41',
'48',
'128',
'252',
'65',
'144',
'149',
'138',
'137',
'136',
'131',
'56',
'76',
'130',
'40',
'122',
'126',
'113',
'129',
'155',
'253',
'268',
'272',
'235',
'209',
'250',
'204',
'28',
'231',
'220',
'238',
'194',
'212',
'206',
'216',
'219',
'263',
'52',
'73',
'47',
'159',
'134',
'66',
'171',
'177',
'156',
'153',
'172',
'154',
'243',
'279',
'19',
'273',
'181',
'202',
'192',
'230',
'201',
'54',
'79',
'63',
'182'
]


for i,j in zip(package_names,xpath):
    print ("""def {defination_name}_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_{no_1}'][name^='jform[groups][]'][type='checkbox'][value='{no_2}']").get_attribute("checked")
    if not isChecked == 'true':
        {name_1} = driver.find_element_by_xpath('//*[@id="1group_{no_3}"]')
        driver.execute_script("arguments[0].click();", {name_2})

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()""".format(defination_name=i, no_1=j, no_2=j, no_3=j, name_1=i, name_2=i))
    print ('\n')


