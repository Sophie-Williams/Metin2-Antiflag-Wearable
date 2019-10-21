// 0.1.) Find this: ENABLE_COSTUME_SYSTEM
// 0.2.) Add after this:
#ifdef ENABLE_ANTIFLAG_WEARABLE
	PyModule_AddIntConstant(poModule, "ENABLE_ANTIFLAG_WEARABLE", true);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_ANTIFLAG_WEARABLE", false);
#endif