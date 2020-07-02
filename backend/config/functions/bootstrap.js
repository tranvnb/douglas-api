"use strict";

/**
 * An asynchronous bootstrap function that runs before
 * your application gets started.
 *
 * This gives you an opportunity to set up your data model,
 * run jobs, or perform some special logic.
 *
 * See more details here: https://strapi.io/documentation/v3.x/concepts/configurations.html#bootstrap
 */

const setAuthenticatedUserPermissions = async (strapi) => {
  const authenticatedUsers = await strapi
    .query("role", "users-permissions")
    .findOne({ type: "authenticated" });
  authenticatedUsers.permissions.forEach((permission) => {
    if (permission.type === "application") {
      const newPermission = permission;
      newPermission.enabled = true;
      strapi
        .query("permission", "users-permissions")
        .update({ id: newPermission.id }, newPermission);
    }
  });
};

const setPublicUserPermissions = async (strapi) => {
  const publicUsers = await strapi
    .query("role", "users-permissions")
    .findOne({ type: "public" });

  publicUsers.permissions.forEach((permission) => {
    if (
      permission.type === "application" &&
      (permission.action === "count" ||
        permission.action === "find" ||
        permission.action === "findone")
    ) {
      const newPermission = permission;
      newPermission.enabled = true;
      strapi
        .query("permission", "users-permissions")
        .update({ id: newPermission.id }, newPermission);
    }
  });
};

module.exports = async () => {
  await setAuthenticatedUserPermissions(strapi);
  await setPublicUserPermissions(strapi);
};
