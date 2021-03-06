from typing import Any, Callable, Dict, Optional


class OnBuildDirective:
    """
    Base directive class for `on_build` hook.
    """

    @staticmethod
    def on_build(schema: "GraphQLSchema") -> None:
        """
        Hook allowing to update at bake time the schema.
        :param schema: the GraphQLSchema instance to work with.
        """


class OnExecutionDirective:
    """
    Base directive class for `on_***_execution` hooks. Available hooks for
    the moment are:
    * on_field_execution
    * on_argument_execution
    """

    @staticmethod
    async def on_field_execution(
        directive_args: Dict[str, Any],
        next_resolver: Callable,
        parent_result: Optional[Any],
        args: Dict[str, Any],
        ctx: Optional[Dict[str, Any]],
        info: "Info",
    ) -> Any:
        """
        Hook allowing you to alterate the resolution behavior of a field.
        :param directive_args: arguments passed to the directive
        :param next_resolver: next resolver to call
        :param parent_result: parent field's result
        :param args: arguments passed to the field
        :param ctx: context passed to the query execution
        :param info: information related to the execution & field resolve
        :return: Any
        """
        # pylint: disable=unused-argument
        return await next_resolver(parent_result, args, ctx, info)

    @staticmethod
    async def on_argument_execution(
        directive_args: Dict[str, Any],
        next_directive: Callable,
        argument_definition: "GraphQLArgument",
        args: Dict[str, Any],
        ctx: Optional[Dict[str, Any]],
        info: "Info",
    ) -> Any:
        """
        Hook allowing you to alterate the coercition behavior of an argument.
        :param directive_args: arguments passed to the directive
        :param next_directive: next directive to call
        :param argument_definition: the GraphQLArgument instance of the
        argument
        :param args: arguments passed to the field/directive
        :param ctx: context passed to the query execution
        :param info: information related to the execution & field resolve
        :return: Any
        """
        # pylint: disable=unused-argument
        return await next_directive(argument_definition, args, ctx, info)


class OnIntrospectionDirective:
    """
    Base directive class for `on_introspection` hook.
    """

    @staticmethod
    def on_introspection(
        directive_args: Dict[str, Any],
        next_directive: Callable,
        introspected_element: Any,
        ctx: Optional[Dict[str, Any]],
        info: "Info",
    ) -> Any:
        """
        Hook allowing you to alterate the introspection behavior for an
        element.
        :param directive_args: arguments passed to the directive
        :param next_directive: next directive to call
        :param introspected_element: current introspected element
        :param ctx: context passed to the query execution
        :param info: information related to the execution & field resolve
        :return: Any
        """
        # pylint: disable=unused-argument
        return next_directive(introspected_element, ctx, info)


class CommonDirective(
    OnBuildDirective, OnExecutionDirective, OnIntrospectionDirective
):
    """
    Base directive class implementing all defaults hooks behavior.
    """
