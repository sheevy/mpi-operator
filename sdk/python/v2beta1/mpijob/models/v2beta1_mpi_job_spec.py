# coding: utf-8

"""
    mpijob

    Python SDK for MPI-Operator  # noqa: E501

    The version of the OpenAPI document: v2beta1
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from mpijob.configuration import Configuration


class V2beta1MPIJobSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'mpi_implementation': 'str',
        'mpi_replica_specs': 'dict(str, V1ReplicaSpec)',
        'run_policy': 'V1RunPolicy',
        'slots_per_worker': 'int',
        'ssh_auth_mount_path': 'str'
    }

    attribute_map = {
        'mpi_implementation': 'mpiImplementation',
        'mpi_replica_specs': 'mpiReplicaSpecs',
        'run_policy': 'runPolicy',
        'slots_per_worker': 'slotsPerWorker',
        'ssh_auth_mount_path': 'sshAuthMountPath'
    }

    def __init__(self, mpi_implementation=None, mpi_replica_specs=None, run_policy=None, slots_per_worker=None, ssh_auth_mount_path=None, local_vars_configuration=None):  # noqa: E501
        """V2beta1MPIJobSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._mpi_implementation = None
        self._mpi_replica_specs = None
        self._run_policy = None
        self._slots_per_worker = None
        self._ssh_auth_mount_path = None
        self.discriminator = None

        if mpi_implementation is not None:
            self.mpi_implementation = mpi_implementation
        self.mpi_replica_specs = mpi_replica_specs
        if run_policy is not None:
            self.run_policy = run_policy
        if slots_per_worker is not None:
            self.slots_per_worker = slots_per_worker
        if ssh_auth_mount_path is not None:
            self.ssh_auth_mount_path = ssh_auth_mount_path

    @property
    def mpi_implementation(self):
        """Gets the mpi_implementation of this V2beta1MPIJobSpec.  # noqa: E501

        MPIImplementation is the MPI implementation. Options are \"OpenMPI\" (default), \"Intel\" and \"MPICH\".  # noqa: E501

        :return: The mpi_implementation of this V2beta1MPIJobSpec.  # noqa: E501
        :rtype: str
        """
        return self._mpi_implementation

    @mpi_implementation.setter
    def mpi_implementation(self, mpi_implementation):
        """Sets the mpi_implementation of this V2beta1MPIJobSpec.

        MPIImplementation is the MPI implementation. Options are \"OpenMPI\" (default), \"Intel\" and \"MPICH\"".  # noqa: E501

        :param mpi_implementation: The mpi_implementation of this V2beta1MPIJobSpec.  # noqa: E501
        :type mpi_implementation: str
        """

        self._mpi_implementation = mpi_implementation

    @property
    def mpi_replica_specs(self):
        """Gets the mpi_replica_specs of this V2beta1MPIJobSpec.  # noqa: E501

        MPIReplicaSpecs contains maps from `MPIReplicaType` to `ReplicaSpec` that specify the MPI replicas to run.  # noqa: E501

        :return: The mpi_replica_specs of this V2beta1MPIJobSpec.  # noqa: E501
        :rtype: dict(str, V1ReplicaSpec)
        """
        return self._mpi_replica_specs

    @mpi_replica_specs.setter
    def mpi_replica_specs(self, mpi_replica_specs):
        """Sets the mpi_replica_specs of this V2beta1MPIJobSpec.

        MPIReplicaSpecs contains maps from `MPIReplicaType` to `ReplicaSpec` that specify the MPI replicas to run.  # noqa: E501

        :param mpi_replica_specs: The mpi_replica_specs of this V2beta1MPIJobSpec.  # noqa: E501
        :type mpi_replica_specs: dict(str, V1ReplicaSpec)
        """
        if self.local_vars_configuration.client_side_validation and mpi_replica_specs is None:  # noqa: E501
            raise ValueError("Invalid value for `mpi_replica_specs`, must not be `None`")  # noqa: E501

        self._mpi_replica_specs = mpi_replica_specs

    @property
    def run_policy(self):
        """Gets the run_policy of this V2beta1MPIJobSpec.  # noqa: E501


        :return: The run_policy of this V2beta1MPIJobSpec.  # noqa: E501
        :rtype: V1RunPolicy
        """
        return self._run_policy

    @run_policy.setter
    def run_policy(self, run_policy):
        """Sets the run_policy of this V2beta1MPIJobSpec.


        :param run_policy: The run_policy of this V2beta1MPIJobSpec.  # noqa: E501
        :type run_policy: V1RunPolicy
        """

        self._run_policy = run_policy

    @property
    def slots_per_worker(self):
        """Gets the slots_per_worker of this V2beta1MPIJobSpec.  # noqa: E501

        Specifies the number of slots per worker used in hostfile. Defaults to 1.  # noqa: E501

        :return: The slots_per_worker of this V2beta1MPIJobSpec.  # noqa: E501
        :rtype: int
        """
        return self._slots_per_worker

    @slots_per_worker.setter
    def slots_per_worker(self, slots_per_worker):
        """Sets the slots_per_worker of this V2beta1MPIJobSpec.

        Specifies the number of slots per worker used in hostfile. Defaults to 1.  # noqa: E501

        :param slots_per_worker: The slots_per_worker of this V2beta1MPIJobSpec.  # noqa: E501
        :type slots_per_worker: int
        """

        self._slots_per_worker = slots_per_worker

    @property
    def ssh_auth_mount_path(self):
        """Gets the ssh_auth_mount_path of this V2beta1MPIJobSpec.  # noqa: E501

        SSHAuthMountPath is the directory where SSH keys are mounted. Defaults to \"/root/.ssh\".  # noqa: E501

        :return: The ssh_auth_mount_path of this V2beta1MPIJobSpec.  # noqa: E501
        :rtype: str
        """
        return self._ssh_auth_mount_path

    @ssh_auth_mount_path.setter
    def ssh_auth_mount_path(self, ssh_auth_mount_path):
        """Sets the ssh_auth_mount_path of this V2beta1MPIJobSpec.

        SSHAuthMountPath is the directory where SSH keys are mounted. Defaults to \"/root/.ssh\".  # noqa: E501

        :param ssh_auth_mount_path: The ssh_auth_mount_path of this V2beta1MPIJobSpec.  # noqa: E501
        :type ssh_auth_mount_path: str
        """

        self._ssh_auth_mount_path = ssh_auth_mount_path

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V2beta1MPIJobSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2beta1MPIJobSpec):
            return True

        return self.to_dict() != other.to_dict()
