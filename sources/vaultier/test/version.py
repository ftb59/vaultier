from django.test.testcases import TransactionTestCase
from django.utils import unittest
from django.utils.unittest.suite import TestSuite
from vaultier.models.vault.model import Vault
from vaultier.models.version.model import Version
from vaultier.test.auth_tools import auth_api_call, register_api_call
from vaultier.test.vault_tools import create_vault_api_call, delete_vault_api_call, update_vault_api_call
from vaultier.test.workspace_tools import create_workspace_api_call


class VersionTest(TransactionTestCase):


    def test_010_current_user(self):

        # create user
        email = 'jan@rclick.cz'
        register_api_call(email=email, nickname='Misan').data
        user1token = auth_api_call(email=email).data.get('token')

        # create workspace
        workspace = create_workspace_api_call(user1token, name='Workspace').data

        #create vault and update vault
        vault_id = create_vault_api_call(user1token, name="vault_in_workspace", workspace=workspace.get('id')).data.get('id')
        update_vault_api_call(user1token, vault_id, name="renamed_vault_in_workspace");

        self.assertEquals(
            Vault.objects.all()[0].name,
            'renamed_vault_in_workspace'
        )


        delete_vault_api_call(user1token, 1)

        vault = Vault.objects.include_deleted().get(pk=1)
        version = Version.objects.get(pk=1);

        pass




def version_suite():
    suite = TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(VersionTest))
    return suite